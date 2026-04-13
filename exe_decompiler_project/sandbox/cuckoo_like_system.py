from sandbox.vm_sandbox import VMSandbox
from sandbox.vm_monitor import VMMonitor
import time

class CuckooLikeSystem:
    def __init__(self):
        self.vm = VMSandbox()
        self.monitor = VMMonitor()

    def analyze(self, file_path):
        result = {
            "vm_execution": None,
            "behavior_logs": None,
            "summary": {}
        }

        # Start VM
        self.vm.start_vm()

        # Run malware
        exec_result = self.vm.run_file(file_path)
        result["vm_execution"] = exec_result

        # Monitor behavior
        logs = self.monitor.monitor(duration=15, interval=3)
        result["behavior_logs"] = logs

        # Stop VM
        self.vm.stop_vm()

        # Simple analysis
        suspicious = 0

        for p in logs["processes"]:
            if "cmd.exe" in p or "powershell" in p:
                suspicious += 1

        for n in logs["network"]:
            if "ESTABLISHED" in n:
                suspicious += 1

        result["summary"] = {
            "suspicious_score": suspicious,
            "risk": "HIGH" if suspicious > 3 else "MEDIUM" if suspicious > 1 else "LOW"
        }

        return result


if __name__ == "__main__":
    system = CuckooLikeSystem()
    output = system.analyze("C:\\malware.exe")
    print(output)
