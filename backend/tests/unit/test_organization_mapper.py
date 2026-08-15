from flowcore.modules.organizations.domain.entities import Organization
from flowcore.modules.organizations.infrastructure.mapper import (
    entity_to_model,
    model_to_entity,
)
from flowcore.modules.organizations.infrastructure.models import (
    OrganizationModel,
)


def test_model_to_entity() -> None:
    model = OrganizationModel(
        id=1,
        name="Acme",
    )

    entity = model_to_entity(model)

    assert isinstance(entity, Organization)
    assert entity.id == 1
    assert entity.name == "Acme"


def test_entity_to_model() -> None:
    entity = Organization(
        id=1,
        name="Acme",
    )

    model = entity_to_model(entity)

    assert isinstance(model, OrganizationModel)
    assert model.id == 1
    assert model.name == "Acme"