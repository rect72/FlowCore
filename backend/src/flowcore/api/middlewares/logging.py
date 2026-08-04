import time
from uuid import uuid4

from fastapi import Request
from starlette.responses import Response


async def logging_middleware(
    request: Request,
    call_next,
) -> Response:
    request_id = request.headers.get("X-Request-ID", str(uuid4()))

    request.state.request_id = request_id

    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = (time.perf_counter() - start_time) * 1000

    response.headers["X-Request-ID"] = request_id

    print(
        f"request_id={request_id} "
        f"{request.method} {request.url.path} - "
        f"{response.status_code} - "
        f"{process_time:.2f} ms"
    )

    return response