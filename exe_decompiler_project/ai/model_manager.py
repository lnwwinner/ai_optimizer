import joblib
import os

class ModelManager:
    def __init__(self, model_path="models/malware_model.pkl"):
        self.model_path = model_path
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

    def save(self, model):
        joblib.dump(model, self.model_path)
        return f"Model saved to {self.model_path}"

    def load(self):
        if not os.path.exists(self.model_path):
            return None
        return joblib.load(self.model_path)
