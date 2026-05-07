from fastapi import FastAPI
from app.api.v1.endpoints.predict import router as predict_router
from app.middleware.logging import LoggingMiddleware
from app.middleware.errors import ErrorMiddleware
from app.middleware.metrics import MetricsMiddleware, metrics_endpoint
from prometheus_client import Counter, Histogram
import time



def create_application() -> FastAPI:
    app = FastAPI(
        title="MLP Letter Classifier API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
   
   # Middlewares
    app.add_middleware(ErrorMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(MetricsMiddleware)
    
  # Routers  
    app.include_router(predict_router, prefix="/v1")
  
  # Metrics endpoint
    app.add_api_route("/metrics", metrics_endpoint, methods=["GET"])












    return app


app = create_application()
