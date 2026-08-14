from flowcore.modules.organizations.application.exceptions import (
    OrganizationNotFoundError,
)
from flowcore.modules.organizations.domain.repository import (
    OrganizationRepository,
)
from flowcore.modules.organizations.infrastructure.models import (
    OrganizationModel,
)


async def create_organization_service(
    repository: OrganizationRepository,
    name: str,
) -> OrganizationModel:
    organization = await repository.create(name)

    return organization


async def get_organizations_service(
    repository: OrganizationRepository,
) -> list[OrganizationModel]:
    organizations = await repository.get_all()

    return organizations


async def get_organization_service(
    repository: OrganizationRepository,
    organization_id: int,
) -> OrganizationModel:
    organization = await repository.get_by_id(organization_id)

    if organization is None:
        raise OrganizationNotFoundError

    return organization


async def update_organization_service(
    repository: OrganizationRepository,
    organization: OrganizationModel,
    name: str,
) -> OrganizationModel:
    updated_organization = await repository.update(
        organization=organization,
        name=name,
    )

    return updated_organization


async def delete_organization_service(
    repository: OrganizationRepository,
    organization: OrganizationModel,
) -> None:
    await repository.delete(organization)