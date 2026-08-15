from fastapi import FastAPI

from flowcore.api.errors import register_exception_handlers
from flowcore.api.middlewares.logging import logging_middleware
from flowcore.api.router import api_router
from flowcore.core.config import settings
from flowcore.core.logging import setup_logging

from flowcore.modules.organizations.application.exceptions import (
    OrganizationNameNotAllowedError,
    OrganizationNotFoundError,
)

from flowcore.modules.organizations.presentation.api.router import (
    organization_name_not_allowed_handler,
    organization_not_found_handler,
)

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.add_exception_handler(
        OrganizationNotFoundError,
        organization_not_found_handler,
    )

    app.add_exception_handler(
        OrganizationNameNotAllowedError,
        organization_name_not_allowed_handler,
    )

    app.middleware("http")(logging_middleware)
    app.include_router(api_router)
    register_exception_handlers(app)

    return app