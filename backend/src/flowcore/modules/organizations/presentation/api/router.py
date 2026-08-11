from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.api.dependencies.common import get_db

from flowcore.modules.organizations.presentation.api.schemas import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
)


from flowcore.modules.organizations.infrastructure.repository import (
    create_organization,
    delete_organization,
    get_organization_by_id,
    get_organizations,
    update_organization,
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

@router.patch(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
async def update_organization_endpoint(
    organization_id: int,
    data: OrganizationUpdate,
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

    updated_organization = await update_organization(
        db=db,
        organization=organization,
        name=data.name,
    )

    return OrganizationResponse.model_validate(updated_organization)

@router.delete(
    "/{organization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_organization_endpoint(
    organization_id: int,
    db: AsyncSession = Depends(get_db),
) -> None:
    organization = await get_organization_by_id(
        db=db,
        organization_id=organization_id,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found.",
        )

    await delete_organization(
        db=db,
        organization=organization,
    )