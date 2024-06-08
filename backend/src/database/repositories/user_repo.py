from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.src.security.auth_security import get_password_hash
from backend.src.common.convert.user import convert_user_schema_to_model
from backend.src.api.v1.user.models import UserModel
from backend.src.api.v1.user.schemas import UserSchema


class UserRepo:
    async def try_create_user(self, data: UserSchema, db: AsyncSession) -> dict:
        data.password = get_password_hash(data.password)
        user = convert_user_schema_to_model(data)

        db.add(user)
        await db.commit()
        await db.refresh(user)

        response = {
            'name': user.name,
            'email': user.email,
        }

        return response

    async def try_get_user(self, username: str, db: AsyncSession) -> Optional[UserModel]:
        stmt = (
            select(UserModel).
            filter(UserModel.name == username)
        )
        result = await db.execute(stmt)
        user = result.scalar()

        return user
