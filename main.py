import tkinter as tk

from sysinfo.sysinfoui import SystemInfoUi


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Information")
        self.geometry("500x450")

        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows += 1
        info = SystemInfoUi(self)
        info.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        self.resizable(False, False)


if __name__ == '__main__':
    try:
        app = App()
        app.tk.call("source", "sun-valley.tcl")
        app.tk.call("set_theme", "dark")
        app.mainloop()
    except KeyboardInterrupt:
        print("\n\nExiting...")
