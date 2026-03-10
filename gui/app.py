import os
import subprocess
import sys
import tkinter as tk


class ControllerGUI(tk.Tk):
    """Simple Tkinter wrapper to start/stop the system without a terminal."""

    def __init__(self):
        super().__init__()
        self.title("Indoor Navigation Controller")
        self.geometry("300x120")

        btn_frame = tk.Frame(self)
        btn_frame.pack(expand=True, pady=20)

        start_btn = tk.Button(btn_frame, text="Start All", width=10, command=self.start_all)
        stop_btn = tk.Button(btn_frame, text="Stop All", width=10, command=self.stop_all)

        start_btn.grid(row=0, column=0, padx=10)
        stop_btn.grid(row=0, column=1, padx=10)

        self.log = tk.Text(self, height=4, state="disabled")
        self.log.pack(fill="x", padx=5, pady=5)

    def append_log(self, text: str):
        self.log.configure(state="normal")
        self.log.insert("end", text + "\n")
        self.log.configure(state="disabled")
        self.log.see("end")

    def run_cmd(self, args):
        try:
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.append_log(f"Launched: {' '.join(args)} (pid {proc.pid})")
        except Exception as e:
            self.append_log(f"Error: {e}")

    def start_all(self):
        self.run_cmd([sys.executable, os.path.join("launch", "manage.py"), "start"])

    def stop_all(self):
        self.run_cmd([sys.executable, os.path.join("launch", "manage.py"), "stop"])


if __name__ == "__main__":
    ControllerGUI().mainloop()
