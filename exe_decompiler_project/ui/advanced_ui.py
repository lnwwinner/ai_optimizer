import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import threading

class AdvancedDecompilerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Decompiler - Advanced UI")
        self.root.geometry("1200x800")

        self.file_path = tk.StringVar()

        top_frame = tk.Frame(root)
        top_frame.pack(fill="x")

        tk.Entry(top_frame, textvariable=self.file_path, width=100).pack(side="left", padx=5)
        tk.Button(top_frame, text="Browse", command=self.browse).pack(side="left")
        tk.Button(top_frame, text="Run", command=self.run_analysis).pack(side="left", padx=5)

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True)

        self.asm_tab = tk.Text(self.tabs)
        self.func_tab = tk.Text(self.tabs)

        self.tabs.add(self.asm_tab, text="Disassembly")
        self.tabs.add(self.func_tab, text="Functions")

    def browse(self):
        file = filedialog.askopenfilename(filetypes=[("EXE", "*.exe")])
        if file:
            self.file_path.set(file)

    def run_analysis(self):
        thread = threading.Thread(target=self.analyze)
        thread.start()

    def analyze(self):
        file = self.file_path.get()
        if not file:
            return

        try:
            asm = subprocess.check_output(["r2", "-A", "-c", "pd 100", file])
            funcs = subprocess.check_output(["r2", "-A", "-c", "afl", file])

            self.asm_tab.insert("end", asm.decode())
            self.func_tab.insert("end", funcs.decode())

        except Exception as e:
            self.asm_tab.insert("end", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedDecompilerUI(root)
    root.mainloop()
