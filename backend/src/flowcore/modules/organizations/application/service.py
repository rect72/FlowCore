from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.modules.organizations.infrastructure.models import (
    OrganizationModel,
)

from flowcore.modules.organizations.infrastructure.repository import (
    create_organization,
    delete_organization,
    get_organization_by_id,
    get_organizations,
    update_organization,
)

from flowcore.modules.organizations.application.exceptions import (
    OrganizationNotFoundError,
)

async def create_organization_service(
    db: AsyncSession,
    name: str,
) -> OrganizationModel:
    organization = await create_organization(
        db=db,
        name=name,
    )

    return organization

async def get_organization_service(
    db: AsyncSession,
    organization_id: int,
) -> OrganizationModel:
    organization = await get_organization_by_id(
        db=db,
        organization_id=organization_id,
    )

    if organization is None:
        raise OrganizationNotFoundError

    return organization

async def update_organization_service(
    db: AsyncSession,
    organization: OrganizationModel,
    name: str,
) -> OrganizationModel:
    updated_organization = await update_organization(
        db=db,
        organization=organization,
        name=name,
    )

    return updated_organization


async def delete_organization_service(
    db: AsyncSession,
    organization: OrganizationModel,
) -> None:
    await delete_organization(
        db=db,
        organization=organization,
    )

async def get_organizations_service(
    db: AsyncSession,
) -> list[OrganizationModel]:
    organizations = await get_organizations(db)

    return organizations