from collections.abc import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.core.config import Settings, get_settings
from flowcore.core.database import SessionFactory

from flowcore.modules.organizations.domain.repository import (
    OrganizationRepository,
)
from flowcore.modules.organizations.infrastructure.repository import (
    SQLAlchemyOrganizationRepository,
)

def get_app_settings() -> Settings:
    return get_settings()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session:
        yield session

async def get_organization_repository(
    db: AsyncSession = Depends(get_db),
) -> OrganizationRepository:
    return SQLAlchemyOrganizationRepository(db)