from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.api.dependencies.common import get_db

from flowcore.modules.organizations.presentation.api.schemas import (
    OrganizationCreate,
    OrganizationResponse,
)


from flowcore.modules.organizations.infrastructure.repository import (
    create_organization,
    get_organization_by_id,
    get_organizations,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_organization_endpoint(
    data: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
) -> OrganizationResponse:
    organization = await create_organization(
        db=db,
        name=data.name,
    )

    return OrganizationResponse.model_validate(organization)

@router.get(
    "",
    response_model=list[OrganizationResponse],
)
async def get_organizations_endpoint(
    db: AsyncSession = Depends(get_db),
) -> list[OrganizationResponse]:
    organizations = await get_organizations(db)

    return [
        OrganizationResponse.model_validate(organization)
        for organization in organizations
    ]

@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
async def get_organization_endpoint(
    organization_id: int,
    db: AsyncSession = Depends(get_db),
) -> OrganizationResponse:
    organization = await get_organization_by_id(
        db=db,
        organization_id=organization_id,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found.",
        )

    return OrganizationResponse.model_validate(organization)