import os
import json
from ai.malware_classifier import MalwareClassifier
from ai.model_manager import ModelManager

class AutoTrainer:
    def __init__(self, dataset_path="dataset/"):
        self.dataset_path = dataset_path
        self.classifier = MalwareClassifier()
        self.model_manager = ModelManager()

    def load_dataset(self):
        reports = []
        labels = []

        for file in os.listdir(self.dataset_path):
            if file.endswith(".json"):
                with open(os.path.join(self.dataset_path, file), "r") as f:
                    data = json.load(f)
                    reports.append(data["report"])
                    labels.append(data["label"])

        return reports, labels

    def train(self):
        reports, labels = self.load_dataset()

        if not reports:
            return "No dataset found"

        self.classifier.train(reports, labels)
        self.model_manager.save(self.classifier.model)

        return f"Trained on {len(reports)} samples"


if __name__ == "__main__":
    trainer = AutoTrainer()
    print(trainer.train())
