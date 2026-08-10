from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.core.config import Settings, get_settings
from flowcore.core.database import SessionFactory


def get_app_settings() -> Settings:
    return get_settings()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session:
        yield session