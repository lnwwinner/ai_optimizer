import os

class SecurityHardening:

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

    def validate_file(self, file_path):
        if not os.path.exists(file_path):
            return False, "File not found"

        size = os.path.getsize(file_path)

        if size > self.MAX_FILE_SIZE:
            return False, "File too large"

        if not file_path.lower().endswith(".exe"):
            return False, "Invalid file type"

        return True, "OK"

    def safe_execute_check(self, filepath):
        # basic check before sandbox
        dangerous_names = ["system32", "cmd.exe"]
        for d in dangerous_names:
            if d in filepath.lower():
                return False, "Blocked dangerous path"

        return True, "Safe"
