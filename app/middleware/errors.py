from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import json
import uuid


class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        trace_id = str(uuid.uuid4())

        try:
            return await call_next(request)

        except Exception as e:
            print(json.dumps({
                "trace_id": trace_id,
                "event": "unhandled_exception",
                "error": str(e),
            }))

            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Internal server error",
                    "trace_id": trace_id
                }
            )
