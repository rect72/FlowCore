from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from flowcore.api.dependencies.common import get_db

from flowcore.modules.organizations.presentation.api.schemas import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
)

from flowcore.modules.organizations.application.service import (
    create_organization_service,
    delete_organization_service,
    get_organization_service,
    get_organizations_service,
    update_organization_service,
)

from flowcore.modules.organizations.application.exceptions import (
    OrganizationNotFoundError,
)

from fastapi import Request
from fastapi.responses import JSONResponse

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
    organization = await create_organization_service(
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
    organizations = await get_organizations_service(db)

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
    organization = await get_organization_service(
        db=db,
        organization_id=organization_id,
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
    organization = await get_organization_service(
        db=db,
        organization_id=organization_id,
    )

    updated_organization = await update_organization_service(
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
    organization = await get_organization_service(
        db=db,
        organization_id=organization_id,
    )

    await delete_organization_service(
        db=db,
        organization=organization,
    )

async def organization_not_found_handler(
    request: Request,
    exc: OrganizationNotFoundError,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)

    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": "not_found",
                "message": "Organization not found.",
                "request_id": request_id,
            }
        },
    )