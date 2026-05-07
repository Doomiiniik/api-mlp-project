from pydantic import BaseModel, Field, field_validator
from typing import List


class PredictRequest(BaseModel):
    features: List[float] = Field(
        ...,
        description="List of 16 numerical features in the correct order."
    )

    @field_validator("features")
    def validate_length(cls, v):
        if len(v) != 16:
            raise ValueError(f"Expected 16 features, got {len(v)}")
        return v


class PredictResponse(BaseModel):
    predicted_class: str
    probabilities: dict[str, float] | None = None
