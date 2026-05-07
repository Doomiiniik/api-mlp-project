from fastapi import APIRouter
from app.schemas.predict import PredictRequest, PredictResponse
from app.models.inference import run_inference

router = APIRouter()


@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    
    result = run_inference(request.features)

    return PredictResponse(
        predicted_class=result["predicted_class"],
        probabilities=result["probabilities"]
    )
