from typing import Protocol

from flowcore.modules.organizations.infrastructure.models import (
    OrganizationModel,
)


class OrganizationRepository(Protocol):
    async def get_by_id(
        self,
        organization_id: int,
    ) -> OrganizationModel | None:
        ...

    async def get_all(
        self,
    ) -> list[OrganizationModel]:
        ...

    async def create(
        self,
        name: str,
    ) -> OrganizationModel:
        ...

    async def update(
        self,
        organization: OrganizationModel,
        name: str,
    ) -> OrganizationModel:
        ...

    async def delete(
        self,
        organization: OrganizationModel,
    ) -> None:
        ...