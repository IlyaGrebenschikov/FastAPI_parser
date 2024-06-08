from fastapi import APIRouter

from backend.src.api.v1.user.routers import user_router


v1_router = APIRouter(
    prefix='/v1',
)
v1_router.include_router(user_router)
