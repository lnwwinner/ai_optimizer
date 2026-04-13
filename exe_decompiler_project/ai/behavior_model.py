import numpy as np
from sklearn.ensemble import RandomForestClassifier

class BehaviorAI:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=150)
        self.trained = False

    def extract_features(self, logs):
        process_count = sum(len(p.splitlines()) for p in logs.get("processes", []))
        network_count = sum(len(n.splitlines()) for n in logs.get("network", []))

        suspicious_proc = sum(1 for p in logs.get("processes", []) if "cmd.exe" in p or "powershell" in p)
        connections = sum(1 for n in logs.get("network", []) if "ESTABLISHED" in n)

        return np.array([
            process_count,
            network_count,
            suspicious_proc,
            connections
        ])

    def train(self, logs_list, labels):
        X = np.array([self.extract_features(l) for l in logs_list])
        y = np.array(labels)
        self.model.fit(X, y)
        self.trained = True

    def predict(self, logs):
        if not self.trained:
            return "Model not trained"
        features = self.extract_features(logs).reshape(1, -1)
        return self.model.predict(features)[0]
