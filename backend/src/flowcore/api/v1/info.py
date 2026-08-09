from fastapi import APIRouter, Depends

from flowcore.api.dependencies.common import get_app_settings
from flowcore.api.schemas.app_info import AppInfoResponse
from flowcore.core.config import Settings


router = APIRouter(tags=["System"])


@router.get("/info", response_model=AppInfoResponse)
def app_info(
    settings: Settings = Depends(get_app_settings),
) -> AppInfoResponse:
    return AppInfoResponse(
        name=settings.app_name,
        version=settings.app_version,
    )