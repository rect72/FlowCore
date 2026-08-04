from fastapi import FastAPI

from flowcore.api.errors import register_exception_handlers
from flowcore.api.middlewares.logging import logging_middleware
from flowcore.api.router import api_router
from flowcore.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.middleware("http")(logging_middleware)
    app.include_router(api_router)
    register_exception_handlers(app)

    return app