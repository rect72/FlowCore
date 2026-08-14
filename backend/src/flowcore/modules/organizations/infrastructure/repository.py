from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.modules.organizations.infrastructure.models import OrganizationModel


class SQLAlchemyOrganizationRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_by_id(
        self,
        organization_id: int,
    ) -> OrganizationModel | None:
        result = await self.db.execute(
            select(OrganizationModel).where(
                OrganizationModel.id == organization_id
            )
        )

        return result.scalar_one_or_none()

    async def get_all(
        self,
    ) -> list[OrganizationModel]:
        result = await self.db.execute(
            select(OrganizationModel)
        )

        return list(result.scalars().all())

    async def create(
        self,
        name: str,
    ) -> OrganizationModel:
        organization = OrganizationModel(name=name)

        self.db.add(organization)

        await self.db.commit()
        await self.db.refresh(organization)

        return organization

    async def update(
        self,
        organization: OrganizationModel,
        name: str,
    ) -> OrganizationModel:
        organization.name = name

        await self.db.commit()
        await self.db.refresh(organization)

        return organization

    async def delete(
        self,
        organization: OrganizationModel,
    ) -> None:
        await self.db.delete(organization)
        await self.db.commit()