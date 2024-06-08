from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from fastapi import status

from backend.src.api.v1.user.models import UserModel
from backend.src.api.v1.user.schemas import UserSchema
from backend.src.database.repositories.user_repo import UserRepo
from backend.src.security.auth_security import verify_password


async def service_create_user(data: UserSchema, db: AsyncSession) -> Optional[dict]:
    user_repo = UserRepo()

    try:
        result = await user_repo.try_create_user(data, db)
        return result
    except Exception:
        raise HTTPException(status_code=400, detail='User already exists')


async def service_get_user(username: str, password: str, db: AsyncSession) -> Optional[UserModel]:
    user_repo = UserRepo()
    exc = HTTPException(status_code=400, detail="Incorrect username or password")

    user = await user_repo.try_get_user(username, db)
    if not user:
        raise exc

    is_password_correct = verify_password(password, user.hashed_password)
    if not is_password_correct:
        raise exc

    return user


async def service_get_user_username(username: str, db: AsyncSession):
    user_repo = UserRepo()

    user = await user_repo.try_get_user(username, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your username is not auth",
        )

    return user
