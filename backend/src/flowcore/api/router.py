from fastapi import APIRouter

from flowcore.api.v1.info import router as info_router
from flowcore.api.v1.system import router as system_router


api_router = APIRouter()

api_router.include_router(
    system_router,
    prefix="/api/v1",
)

api_router.include_router(
    info_router,
    prefix="/api/v1",
)