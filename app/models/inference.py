import torch
from typing import List
from app.models.loader import ModelLoader


def run_inference(features: List[float]) -> dict:
    model = ModelLoader.load_model()

    x = torch.tensor(features, dtype=torch.float32).unsqueeze(0)

    with torch.no_grad():
        logits = model(x)
        probs = torch.softmax(logits, dim=1).squeeze().tolist()

    pred_idx = int(torch.argmax(logits, dim=1).item())
    prob_dict = {str(i): float(p) for i, p in enumerate(probs)}

    return {
        "predicted_class": str(pred_idx),
        "probabilities": prob_dict
    }
