import os
import PyInstaller.__main__

APP_NAME = "AI_Decompiler"
ENTRY_FILE = "ui/advanced_ui.py"

PyInstaller.__main__.run([
    ENTRY_FILE,
    '--name=%s' % APP_NAME,
    '--onefile',
    '--windowed',
    '--icon=NONE',
])

print("Build complete. Check dist/ folder.")
