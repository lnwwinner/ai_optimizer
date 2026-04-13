import json
import os
from ai.xgboost_model import XGBoostMalwareClassifier
from ai.behavior_model import BehaviorAI

class AutoFeedbackLoop:
    def __init__(self, reports_dir="reports/"):
        self.reports_dir = reports_dir
        self.static_model = XGBoostMalwareClassifier()
        self.behavior_model = BehaviorAI()

    def load_reports(self):
        data = []
        for file in os.listdir(self.reports_dir):
            if file.endswith(".json"):
                with open(os.path.join(self.reports_dir, file)) as f:
                    data.append(json.load(f))
        return data

    def auto_label(self, report):
        score = report.get("summary", {}).get("suspicious_score", 0)
        if score > 3:
            return "Malware"
        elif score > 1:
            return "Suspicious"
        else:
            return "Benign"

    def retrain(self):
        reports = self.load_reports()

        static_data = []
        behavior_data = []
        labels = []

        for r in reports:
            label = self.auto_label(r)
            labels.append(label)

            # fake structure mapping (adapt if needed)
            static_data.append(r.get("summary", {}))
            behavior_data.append(r.get("behavior_logs", {}))

        if static_data:
            self.static_model.train(static_data, labels)

        if behavior_data:
            self.behavior_model.train(behavior_data, labels)

        return f"Retrained on {len(labels)} samples"


if __name__ == "__main__":
    loop = AutoFeedbackLoop()
    print(loop.retrain())
