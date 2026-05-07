import json
import torch
from pathlib import Path
from threading import Lock
from app.models.architecture import MLP


CONFIG_PATH = "configs/best_config.json"
MODEL_PATH = "models/best_model.pt"


class ModelLoader:
    _model = None
    _lock = Lock()

    @classmethod
    def load_model(cls):
        """
        Lazy, thread-safe loader.
        Rebuilds model from config + loads state_dict.
        """
        if cls._model is None:
            with cls._lock:
                if cls._model is None:

                    # Load config
                    config_file = Path(CONFIG_PATH)
                    if not config_file.exists():
                        raise FileNotFoundError(f"Config not found: {CONFIG_PATH}")

                    with open(config_file, "r") as f:
                        config = json.load(f)

                    input_dim = config["input_dim"]
                    hidden_layers = config["hidden_layers"]
                    output_dim = config["output_dim"]
                    dropout = config.get("dropout", 0.0)

                    # Build model
                    model = MLP(
                        input_dim=input_dim,
                        hidden_layers=hidden_layers,
                        output_dim=output_dim,
                        dropout=dropout
                    )

                    # Load weights
                    model_path = Path(MODEL_PATH)
                    if not model_path.exists():
                        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

                    state_dict = torch.load(model_path, map_location="cpu")
                    model.load_state_dict(state_dict)
                    model.eval()

                    cls._model = model

        return cls._model
