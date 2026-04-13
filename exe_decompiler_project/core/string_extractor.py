import re

class StringExtractor:
    def __init__(self):
        pass

    def extract_strings(self, file_path, min_length=4):
        with open(file_path, "rb") as f:
            data = f.read()

        pattern = rb"[\x20-\x7E]{%d,}" % min_length
        strings = re.findall(pattern, data)

        decoded = [s.decode(errors="ignore") for s in strings]
        return decoded

    def analyze_strings(self, strings):
        result = {
            "urls": [],
            "ips": [],
            "commands": []
        }

        for s in strings:
            if "http" in s or "www" in s:
                result["urls"].append(s)

            if re.match(r"\d+\.\d+\.\d+\.\d+", s):
                result["ips"].append(s)

            if any(cmd in s.lower() for cmd in ["cmd", "powershell", "bash"]):
                result["commands"].append(s)

        return result
