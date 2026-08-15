from flowcore.modules.organizations.application.exceptions import (
    OrganizationNameNotAllowedError,
    OrganizationNotFoundError,
)
from flowcore.modules.organizations.domain.repository import (
    OrganizationRepository,
)

from flowcore.modules.organizations.domain.entities import Organization


async def create_organization_service(
    repository: OrganizationRepository,
    name: str,
) -> Organization:
    forbidden_names = {"admin", "system"}

    if name.lower() in forbidden_names:
        raise OrganizationNameNotAllowedError

    organization = await repository.create(name)

    return organization


async def get_organizations_service(
    repository: OrganizationRepository,
) -> list[Organization]:
    organizations = await repository.get_all()

    return organizations


async def get_organization_service(
    repository: OrganizationRepository,
    organization_id: int,
) -> Organization:
    organization = await repository.get_by_id(organization_id)

    if organization is None:
        raise OrganizationNotFoundError

    return organization


async def update_organization_service(
    repository: OrganizationRepository,
    organization: Organization,
    name: str,
) -> Organization:
    updated_organization = await repository.update(
        organization=organization,
        name=name,
    )

    return updated_organization


async def delete_organization_service(
    repository: OrganizationRepository,
    organization: Organization,
) -> None:
    await repository.delete(organization)