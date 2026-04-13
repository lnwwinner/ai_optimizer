# EXE Decompiler Project

Advanced Python-based EXE analysis and decompilation framework.

## Features
- Static analysis (PE headers, imports)
- Disassembly (Capstone)
- Decompilation integration (Ghidra / Radare2)
- AI-assisted code reconstruction (future)

## Structure
- core/ -> analysis engine
- decompiler/ -> decompile logic
- ai/ -> ML reconstruction
- ui/ -> optional interface

## Usage
```bash
python main.py --file sample.exe
```
