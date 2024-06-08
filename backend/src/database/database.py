from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.core.settings import get_db_settings


engine = create_async_engine(url=get_db_settings().create_url_obj())
async_session = async_sessionmaker(engine, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
