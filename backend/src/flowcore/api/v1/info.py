from fastapi import APIRouter, Depends

from flowcore.api.dependencies.common import get_app_settings, get_db
from flowcore.api.schemas.app_info import AppInfoResponse
from flowcore.core.config import Settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

router = APIRouter(tags=["System"])


@router.get("/info", response_model=AppInfoResponse)
def app_info(
    settings: Settings = Depends(get_app_settings),
) -> AppInfoResponse:
    return AppInfoResponse(
        name=settings.app_name,
        version=settings.app_version,
    )

@router.get("/db-check")
async def db_check(
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    await db.execute(text("SELECT 1"))

    return {
        "status": "database_connected"
    }