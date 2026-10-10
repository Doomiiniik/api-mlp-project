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

        for i,x in enumerate(v):
            if x>15 or x<0:
                raise ValueError(f"Feature not in <0,15> range on {i+1} postion")


        
        
        return v


class PredictResponse(BaseModel):
    predicted_class: str
    probabilities: dict[str, float] | None = None
