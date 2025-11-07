import json
import os

def aggregate_scores(grammar: float, fluency: float, pron: float) -> float:
    """
    Weighted score using models/scoring_config.json
    """
    config_path = os.path.join("models", "scoring_config.json")

    try:
        with open(config_path, "r") as f:
            cfg = json.load(f)
    except Exception:
        cfg = {"grammar_weight": 0.6, "fluency_weight": 0.3, "pron_weight": 0.1}

    w_g = cfg["grammar_weight"]
    w_f = cfg["fluency_weight"]
    w_p = cfg["pron_weight"]

    score = grammar * w_g + fluency * w_f + pron * w_p
    return round(score, 2)
