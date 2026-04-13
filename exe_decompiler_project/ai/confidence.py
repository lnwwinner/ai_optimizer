class ConfidenceScorer:

    def calculate(self, static_prob=0.5, behavior_prob=0.5):
        score = (static_prob * 0.6) + (behavior_prob * 0.4)

        if score > 0.8:
            level = "HIGH"
        elif score > 0.5:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "confidence": round(score, 3),
            "level": level
        }
