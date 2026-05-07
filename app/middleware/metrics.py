from prometheus_client import Counter, Histogram, generate_latest
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import time


REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds",
    "API request latency",
    ["endpoint"]
)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = time.time() - start

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()

        REQUEST_LATENCY.labels(
            endpoint=request.url.path
        ).observe(duration)

        return response


def metrics_endpoint():
    return Response(generate_latest(), media_type="text/plain")
