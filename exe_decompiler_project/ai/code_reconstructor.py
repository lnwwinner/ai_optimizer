import re

class CodeReconstructor:
    def __init__(self):
        pass

    def reconstruct(self, asm_code: str) -> str:
        lines = asm_code.split("\n")
        pseudo_code = []

        for line in lines:
            line = line.strip()

            # Simple patterns
            if "cmp" in line and "jl" in line:
                pseudo_code.append("if condition < value:")
            elif "cmp" in line and "jg" in line:
                pseudo_code.append("if condition > value:")
            elif "je" in line:
                pseudo_code.append("if equal:")
            elif "jne" in line:
                pseudo_code.append("if not equal:")
            elif "call" in line:
                func = line.split("call")[-1].strip()
                pseudo_code.append(f"call_function({func})")
            elif "mov" in line:
                parts = re.split(r'[ ,]+', line)
                if len(parts) >= 3:
                    pseudo_code.append(f"{parts[1]} = {parts[2]}")

        return "\n".join(pseudo_code)


if __name__ == "__main__":
    sample = """
    mov eax, 5
    cmp eax, 10
    jl 0x401000
    call printf
    """

    recon = CodeReconstructor()
    print(recon.reconstruct(sample))
