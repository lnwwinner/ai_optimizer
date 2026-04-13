from sandbox.cuckoo_like_system import CuckooLikeSystem
import os
import json
import time

class SandboxOrchestrator:
    def __init__(self, samples_dir="samples/", reports_dir="reports/"):
        self.system = CuckooLikeSystem()
        self.samples_dir = samples_dir
        self.reports_dir = reports_dir
        os.makedirs(self.reports_dir, exist_ok=True)

    def process_all(self):
        results = []

        for file in os.listdir(self.samples_dir):
            if file.endswith(".exe"):
                path = os.path.join(self.samples_dir, file)
                print(f"[+] Analyzing {file}")

                result = self.system.analyze(path)

                report_path = os.path.join(self.reports_dir, file + ".json")
                with open(report_path, "w") as f:
                    json.dump(result, f, indent=2)

                results.append({"file": file, "report": report_path})

                time.sleep(2)

        return results


if __name__ == "__main__":
    orch = SandboxOrchestrator()
    output = orch.process_all()
    print(output)
