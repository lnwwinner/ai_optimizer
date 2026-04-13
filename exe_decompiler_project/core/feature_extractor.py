import pefile
import math
import os

class FeatureExtractor:
    def __init__(self):
        pass

    def entropy(self, data):
        if not data:
            return 0
        occurences = [0] * 256
        for x in data:
            occurences[x] += 1
        entropy = 0
        for x in occurences:
            if x == 0:
                continue
            p_x = float(x) / len(data)
            entropy -= p_x * math.log2(p_x)
        return entropy

    def extract(self, file_path):
        features = {
            "file_size": os.path.getsize(file_path),
            "entropy": 0,
            "num_sections": 0,
            "imports": []
        }

        try:
            pe = pefile.PE(file_path)

            # entropy
            with open(file_path, "rb") as f:
                data = f.read()
                features["entropy"] = self.entropy(data)

            # sections
            features["num_sections"] = len(pe.sections)

            # imports
            if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    features["imports"].append(entry.dll.decode(errors="ignore"))

        except Exception as e:
            features["error"] = str(e)

        return features
