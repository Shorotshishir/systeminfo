import tkinter as tk
from tkinter import ttk
from tkinter import font
import yaml

from sysinfo.sysinfo import SystemInfo


class SystemInfoUi(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Consolas",
                                   size=11)
        self.Button_4 = None
        self.InfoLabel = tk.StringVar()
        self.Button_3 = None
        self.Label_1 = None
        self.TextBox_1 = None
        self.Button_1 = None
        self.Button_2 = None
        self.parent = parent
        self.sysinfo = SystemInfo()
        self.init_ui()
        self.view_ram_info()

    def init_ui(self):
        self.Label_1 = ttk.Label(self, textvariable=self.InfoLabel)
        self.Label_1.grid(column=0, row=0, columnspan=8, sticky='W', padx=5, pady=5)

        self.Button_1 = ttk.Button(self, text='Get Ram Info', command=self.view_ram_info)
        self.Button_1.grid(column=9, row=1, columnspan=3, sticky='new', padx=5, pady=5)

        self.Button_2 = ttk.Button(self, text='Get Disk Info', command=self.view_disk_info)
        self.Button_2.grid(column=9, row=2, columnspan=3, sticky='new',padx=5, pady=5)

        self.Button_3 = ttk.Button(self, text='Get Os Info', command=self.view_os_info)
        self.Button_3.grid(column=9, row=3, columnspan=3, sticky='new', padx=5, pady=5)

        self.Button_4 = ttk.Button(self, text='Get CPU Info', command=self.view_cpu_info)
        self.Button_4.grid(column=9, row=4, columnspan=3, sticky='new', padx=5, pady=5)

        self.TextBox_1 = tk.Text(self, height=22, width=45, font=self.defaultFont)
        self.TextBox_1.grid(column=0, row=1, columnspan=8, rowspan=10, sticky='nwe', padx=5, pady=5)

        self.grid(column=10, row=0, sticky='W')

    def view_ram_info(self):
        self.InfoLabel.set('Ram Info')
        ram_info = yaml.dump(self.sysinfo.get_ram_info(), sort_keys=False, default_flow_style=False)
        self.TextBox_1.delete(1.0, tk.END)
        self.TextBox_1.insert(tk.END, ram_info)

    def view_disk_info(self):
        self.InfoLabel.set('Disk Info')
        disk_info = yaml.dump(self.sysinfo.get_disk_info(), sort_keys=False, default_flow_style=False)
        self.TextBox_1.delete(1.0, tk.END)
        self.TextBox_1.insert(tk.END, disk_info)

    def view_os_info(self):
        self.InfoLabel.set('Os Info')
        os_info = yaml.dump(self.sysinfo.get_os_info(), sort_keys=False, default_flow_style=False)
        self.TextBox_1.delete(1.0, tk.END)
        self.TextBox_1.insert(tk.END, os_info)

    def view_cpu_info(self):
        self.InfoLabel.set('CPU Info')
        cpu_info = yaml.dump(self.sysinfo.get_cpu_info(), sort_keys=False, default_flow_style=False)
        self.TextBox_1.delete(1.0, tk.END)
        self.TextBox_1.insert(tk.END, cpu_info)