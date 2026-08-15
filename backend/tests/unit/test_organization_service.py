import pytest

from flowcore.modules.organizations.application.exceptions import (
    OrganizationNameNotAllowedError,
    OrganizationNotFoundError,
)

from flowcore.modules.organizations.application.service import (
    create_organization_service,
    delete_organization_service,
    get_organization_service,
    get_organizations_service,
    update_organization_service,
)

from flowcore.modules.organizations.domain.entities import Organization


class FakeOrganizationRepository:
    def __init__(self) -> None:
        self.organizations: list[Organization] = []
        self.next_id = 1

    async def create(
        self,
        name: str,
    ) -> Organization:
        organization = Organization(
            id=self.next_id,
            name=name,
        )

        self.next_id += 1
        self.organizations.append(organization)

        return organization

    async def get_by_id(
        self,
        organization_id: int,
    ) -> Organization | None:
        for organization in self.organizations:
            if organization.id == organization_id:
                return organization

        return None

    async def get_all(
            self,
    ) -> list[Organization]:
        return self.organizations.copy()

    async def update(
            self,
            organization: Organization,
            name: str,
    ) -> Organization:
        organization.name = name
        return organization

    async def delete(
            self,
            organization: Organization,
    ) -> None:
        self.organizations.remove(organization)

@pytest.mark.anyio
async def test_create_organization_service() -> None:
    repository = FakeOrganizationRepository()

    organization = await create_organization_service(
        repository=repository,
        name="Acme",
    )

    assert organization.id == 1
    assert organization.name == "Acme"

@pytest.mark.anyio
async def test_get_missing_organization_raises_error() -> None:
    repository = FakeOrganizationRepository()

    with pytest.raises(OrganizationNotFoundError):
        await get_organization_service(
            repository=repository,
            organization_id=999,
        )

@pytest.mark.anyio
async def test_get_organizations_service() -> None:
    repository = FakeOrganizationRepository()

    await repository.create("Acme")
    await repository.create("Flow Corp")

    organizations = await get_organizations_service(
        repository=repository,
    )

    assert len(organizations) == 2
    assert organizations[0].name == "Acme"
    assert organizations[1].name == "Flow Corp"

@pytest.mark.anyio
async def test_update_organization_service() -> None:
    repository = FakeOrganizationRepository()

    organization = await repository.create("Old Name")

    updated = await update_organization_service(
        repository=repository,
        organization=organization,
        name="New Name",
    )

    assert updated.name == "New Name"

@pytest.mark.anyio
async def test_delete_organization_service() -> None:
    repository = FakeOrganizationRepository()

    organization = await repository.create("Delete Me")

    await delete_organization_service(
        repository=repository,
        organization=organization,
    )

    assert repository.organizations == []

@pytest.mark.anyio
async def test_create_organization_rejects_forbidden_name() -> None:
    repository = FakeOrganizationRepository()

    with pytest.raises(OrganizationNameNotAllowedError):
        await create_organization_service(
            repository=repository,
            name="admin",
        )

    assert repository.organizations == []