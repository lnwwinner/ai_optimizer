import numpy as np
from xgboost import XGBClassifier
import joblib

class XGBoostMalwareClassifier:
    def __init__(self):
        self.model = XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            use_label_encoder=False,
            eval_metric='mlogloss'
        )
        self.trained = False

    def extract_features(self, report):
        return np.array([
            int(report.get("process_injection", False)),
            int(report.get("network_activity", False)),
            int(report.get("file_operations", False)),
            len(report.get("suspicious_calls", [])),
            report.get("entropy", 0),
            report.get("num_sections", 0),
            report.get("file_size", 0),
            len(report.get("urls", [])),
            len(report.get("ips", [])),
            len(report.get("commands", []))
        ])

    def train(self, reports, labels):
        X = np.array([self.extract_features(r) for r in reports])
        y = np.array(labels)
        self.model.fit(X, y)
        self.trained = True

    def predict(self, report):
        if not self.trained:
            return "Model not trained"
        features = self.extract_features(report).reshape(1, -1)
        return self.model.predict(features)[0]

    def save(self, path="models/xgb_model.pkl"):
        joblib.dump(self.model, path)

    def load(self, path="models/xgb_model.pkl"):
        self.model = joblib.load(path)
        self.trained = True
