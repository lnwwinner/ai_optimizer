import subprocess
import time
import os

class SandboxRunner:
    def __init__(self, timeout=10):
        self.timeout = timeout

    def run(self, file_path):
        report = {
            "executed": False,
            "error": None,
            "runtime": 0
        }

        start = time.time()

        try:
            process = subprocess.Popen(
                [file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            try:
                stdout, stderr = process.communicate(timeout=self.timeout)
                report["executed"] = True
                report["stdout"] = stdout.decode(errors="ignore")
                report["stderr"] = stderr.decode(errors="ignore")

            except subprocess.TimeoutExpired:
                process.kill()
                report["error"] = "Timeout"

        except Exception as e:
            report["error"] = str(e)

        report["runtime"] = time.time() - start
        return report


if __name__ == "__main__":
    runner = SandboxRunner()
    result = runner.run("sample.exe")
    print(result)
