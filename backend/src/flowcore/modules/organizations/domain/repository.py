from typing import Protocol

from flowcore.modules.organizations.domain.entities import Organization


class OrganizationRepository(Protocol):
    async def get_by_id(
        self,
        organization_id: int,
    ) -> Organization | None:
        ...

    async def get_all(
        self,
    ) -> list[Organization]:
        ...

    async def create(
        self,
        name: str,
    ) -> Organization:
        ...

    async def update(
        self,
        organization: Organization,
        name: str,
    ) -> Organization:
        ...

    async def delete(
        self,
        organization: Organization,
    ) -> None:
        ...