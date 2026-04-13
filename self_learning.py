import json
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_FILE = "training_data.json"
MODEL_PATH = "model.pkl"

class SelfLearningModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self._load_or_init()

    def _load_or_init(self):
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            self._init_dataset()

    def _init_dataset(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def add_sample(self, cpu, ram, disk, action):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        data.append({
            "cpu": cpu,
            "ram": ram,
            "disk": disk,
            "action": action
        })

        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

    def train(self):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        if len(data) < 5:
            return

        X = np.array([[d["cpu"], d["ram"], d["disk"]] for d in data])
        y = np.array([d["action"] for d in data])

        self.model.fit(X, y)
        joblib.dump(self.model, MODEL_PATH)

    def predict(self, cpu, ram, disk):
        try:
            return self.model.predict([[cpu, ram, disk]])[0]
        except:
            return 0
