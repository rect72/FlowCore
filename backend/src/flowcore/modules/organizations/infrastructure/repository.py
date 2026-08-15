from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.modules.organizations.infrastructure.models import OrganizationModel

from flowcore.modules.organizations.domain.entities import Organization
from flowcore.modules.organizations.infrastructure.mapper import (
    model_to_entity,
)

class SQLAlchemyOrganizationRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_by_id(
            self,
            organization_id: int,
    ) -> Organization | None:
        result = await self.db.execute(
            select(OrganizationModel).where(
                OrganizationModel.id == organization_id
            )
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return model_to_entity(model)

    async def get_all(
            self,
    ) -> list[Organization]:
        result = await self.db.execute(
            select(OrganizationModel)
        )

        models = result.scalars().all()

        return [
            model_to_entity(model)
            for model in models
        ]

    async def create(
            self,
            name: str,
    ) -> Organization:
        model = OrganizationModel(name=name)

        self.db.add(model)

        await self.db.commit()
        await self.db.refresh(model)

        return model_to_entity(model)

    async def update(
            self,
            organization: Organization,
            name: str,
    ) -> Organization:
        result = await self.db.execute(
            select(OrganizationModel).where(
                OrganizationModel.id == organization.id
            )
        )

        model = result.scalar_one()

        model.name = name

        await self.db.commit()
        await self.db.refresh(model)

        return model_to_entity(model)

    async def delete(
            self,
            organization: Organization,
    ) -> None:
        result = await self.db.execute(
            select(OrganizationModel).where(
                OrganizationModel.id == organization.id
            )
        )

        model = result.scalar_one()

        await self.db.delete(model)
        await self.db.commit()