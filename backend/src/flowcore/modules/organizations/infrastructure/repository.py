from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.modules.organizations.infrastructure.models import OrganizationModel

from sqlalchemy import select

async def create_organization(
    db: AsyncSession,
    name: str,
) -> OrganizationModel:
    organization = OrganizationModel(name=name)

    db.add(organization)

    await db.commit()
    await db.refresh(organization)

    return organization

async def get_organizations(
    db: AsyncSession,
) -> list[OrganizationModel]:
    result = await db.execute(
        select(OrganizationModel)
    )

    return list(result.scalars().all())

async def get_organization_by_id(
    db: AsyncSession,
    organization_id: int,
) -> OrganizationModel | None:
    result = await db.execute(
        select(OrganizationModel).where(
            OrganizationModel.id == organization_id
        )
    )

    return result.scalar_one_or_none()