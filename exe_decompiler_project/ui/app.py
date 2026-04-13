import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
import os

class DecompilerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EXE Decompiler - AI Tool")
        self.root.geometry("900x600")

        self.file_path = tk.StringVar()

        tk.Label(root, text="Select EXE File:").pack()
        tk.Entry(root, textvariable=self.file_path, width=80).pack()
        tk.Button(root, text="Browse", command=self.browse_file).pack()

        tk.Button(root, text="Analyze", command=self.analyze).pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, width=100, height=30)
        self.output.pack()

    def browse_file(self):
        file = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if file:
            self.file_path.set(file)

    def analyze(self):
        file = self.file_path.get()
        if not file:
            self.output.insert(tk.END, "No file selected\n")
            return

        self.output.insert(tk.END, f"Analyzing: {file}\n")

        # Example: call radare2 if installed
        try:
            result = subprocess.check_output(["r2", "-A", "-c", "afl", file], stderr=subprocess.STDOUT)
            self.output.insert(tk.END, result.decode())
        except Exception as e:
            self.output.insert(tk.END, f"Error: {str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DecompilerUI(root)
    root.mainloop()
