from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    if exc.status_code == 404:
        code = "not_found"
        message = "Resource not found."
    else:
        code = "http_error"
        message = str(exc.detail)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code,
                "message": message,
            }
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        StarletteHTTPException,
        http_exception_handler,
    )