import tkinter as tk
from tkinter import ttk


class AppView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('No one Cares')
        self.geometry('600x300')
        self.minsize(600, 300)
        self.resizable(False, True)

        self.frame = ttk.Frame(self, relief=tk.GROOVE)
        self.frame.pack(padx=10, pady=10)
        
        for i in range(3):
            self.frame.columnconfigure(i, weight=1)
        for j in range(5):
            self.frame.rowconfigure(j, weight=1)