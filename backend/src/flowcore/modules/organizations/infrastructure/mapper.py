from flowcore.modules.organizations.domain.entities import Organization
from flowcore.modules.organizations.infrastructure.models import (
    OrganizationModel,
)


def model_to_entity(
    model: OrganizationModel,
) -> Organization:
    return Organization(
        id=model.id,
        name=model.name,
    )


def entity_to_model(
    entity: Organization,
) -> OrganizationModel:
    return OrganizationModel(
        id=entity.id,
        name=entity.name,
    )