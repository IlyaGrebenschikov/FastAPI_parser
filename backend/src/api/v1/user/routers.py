from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.database import get_session
from backend.src.api.v1.user.schemas import UserSchema
from backend.src.api.v1.user.services import service_create_user


user_router = APIRouter(
    tags=['user'],
    prefix='/user',
)


@user_router.post('/create', operation_id='create')
async def create_user(data: UserSchema, db: Annotated[AsyncSession, Depends(get_session)]):
    return await service_create_user(data, db)
