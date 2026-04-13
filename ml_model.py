import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = "model.pkl"

class OptimizerModel:
    def __init__(self):
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            self.model = RandomForestClassifier()
            self._train_dummy()

    def _train_dummy(self):
        X = np.array([
            [90, 80, 95],
            [20, 30, 40],
            [85, 70, 88],
            [10, 20, 30]
        ])
        y = np.array([1, 0, 1, 0])
        self.model.fit(X, y)
        joblib.dump(self.model, MODEL_PATH)

    def predict(self, cpu, ram, disk):
        return self.model.predict([[cpu, ram, disk]])[0]
