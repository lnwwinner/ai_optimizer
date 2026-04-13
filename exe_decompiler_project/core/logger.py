import json
import os
from datetime import datetime

class SystemLogger:
    def __init__(self, log_dir="logs/"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log(self, data):
        filename = datetime.now().strftime("%Y-%m-%d") + ".log"
        path = os.path.join(self.log_dir, filename)

        entry = {
            "timestamp": datetime.now().isoformat(),
            "data": data
        }

        with open(path, "a") as f:
            f.write(json.dumps(entry) + "\n")

        return path
