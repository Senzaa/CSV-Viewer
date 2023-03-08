import tkinter as tk
from tkinter import ttk

class DataGrid(ttk.Frame):
    slots = 'MasterGrid'
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(padx=5, pady=5)
        self.MasterGrid = []

        for row in range(10):
            self.MasterGrid.append([])
            for column in range(10):
                text = tk.Entry(self, justify=tk.CENTER, width=100)
                text.grid(row=row, column=column, sticky="we")
                self.MasterGrid[row].append(text)
                self.grid_columnconfigure(column, weight=1)