import subprocess
import time

class VMSandbox:
    def __init__(self, vm_name="SandboxVM", timeout=30):
        self.vm_name = vm_name
        self.timeout = timeout

    def start_vm(self):
        subprocess.call(["VBoxManage", "startvm", self.vm_name, "--type", "headless"])
        time.sleep(10)

    def run_file(self, guest_path):
        cmd = [
            "VBoxManage", "guestcontrol", self.vm_name,
            "run", "--exe", guest_path,
            "--username", "user",
            "--password", "password",
            "--wait-stdout", "--wait-stderr"
        ]

        try:
            output = subprocess.check_output(cmd, timeout=self.timeout)
            return {"success": True, "output": output.decode(errors="ignore")}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def stop_vm(self):
        subprocess.call(["VBoxManage", "controlvm", self.vm_name, "poweroff"])


if __name__ == "__main__":
    vm = VMSandbox()
    vm.start_vm()
    result = vm.run_file("C:\\malware.exe")
    print(result)
    vm.stop_vm()
