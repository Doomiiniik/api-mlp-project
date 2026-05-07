import time
import uuid
import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        trace_id = str(uuid.uuid4())

        # Log request
        request_body = await request.body()
        try:
            request_data = request_body.decode("utf-8")
        except:
            request_data = "<binary>"

        print(json.dumps({
            "trace_id": trace_id,
            "event": "request",
            "method": request.method,
            "path": request.url.path,
            "query": dict(request.query_params),
            "body": request_data,
        }))

        # Process request
        try:
            response = await call_next(request)
            status = response.status_code
        except Exception as e:
            status = 500
            print(json.dumps({
                "trace_id": trace_id,
                "event": "error",
                "error": str(e),
            }))
            raise e

        # Log response
        duration = round((time.time() - start_time) * 1000, 2)

        print(json.dumps({
            "trace_id": trace_id,
            "event": "response",
            "status": status,
            "duration_ms": duration,
        }))

        return response
