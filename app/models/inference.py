import json
import torch
from typing import List
from app.models.loader import ModelLoader

SCALER_PATH = "configs/scaler.json"

with open(SCALER_PATH, "r") as f:
    _scaler = json.load(f)

MEAN = torch.tensor(_scaler["mean"], dtype=torch.float32)
STD = torch.tensor(_scaler["std"], dtype=torch.float32)


def run_inference(features: List[float]) -> dict:
    model = ModelLoader.load_model()

    x = torch.tensor(features, dtype=torch.float32).unsqueeze(0)
    x = (x - MEAN) / STD  # same scaling as in training (StandardScaler)

    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=1).squeeze().tolist()

    pred_idx = int(torch.argmax(logits, dim=1).item())
    prob_dict = {str(i): float(p) for i, p in enumerate(probs)}

    return {
        "predicted_class": str(pred_idx),
        "probabilities": prob_dict
    }
