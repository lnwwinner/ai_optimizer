import subprocess
import time

class VMMonitor:
    def __init__(self, vm_name="SandboxVM"):
        self.vm_name = vm_name

    def list_processes(self):
        cmd = [
            "VBoxManage", "guestcontrol", self.vm_name,
            "run", "--exe", "cmd.exe",
            "--username", "user",
            "--password", "password",
            "--", "cmd.exe", "/c", "tasklist"
        ]

        try:
            output = subprocess.check_output(cmd)
            return output.decode(errors="ignore")
        except Exception as e:
            return str(e)

    def network_connections(self):
        cmd = [
            "VBoxManage", "guestcontrol", self.vm_name,
            "run", "--exe", "cmd.exe",
            "--username", "user",
            "--password", "password",
            "--", "cmd.exe", "/c", "netstat -an"
        ]

        try:
            output = subprocess.check_output(cmd)
            return output.decode(errors="ignore")
        except Exception as e:
            return str(e)

    def monitor(self, duration=10, interval=2):
        logs = {
            "processes": [],
            "network": []
        }

        for _ in range(duration // interval):
            logs["processes"].append(self.list_processes())
            logs["network"].append(self.network_connections())
            time.sleep(interval)

        return logs


if __name__ == "__main__":
    monitor = VMMonitor()
    data = monitor.monitor()
    print(data)
