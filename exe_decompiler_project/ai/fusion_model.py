import numpy as np

class FusionModel:
    def __init__(self):
        pass

    def combine(self, static_pred, behavior_pred, xgb_score=0.5, behavior_score=0.5):
        score = 0

        if static_pred == "Malware":
            score += xgb_score

        if behavior_pred == "Malware":
            score += behavior_score

        if score >= 0.75:
            return {"final": "HIGH RISK", "score": score}
        elif score >= 0.4:
            return {"final": "MEDIUM RISK", "score": score}
        else:
            return {"final": "LOW RISK", "score": score}


if __name__ == "__main__":
    fusion = FusionModel()
    result = fusion.combine("Malware", "Malware")
    print(result)
