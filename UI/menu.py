import tkinter as tk
from tkinter import ttk

class TopMenu(tk.Menu):
    slots = 'FileMenu', 'EditMenu'
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        # File Menu
        self.FileMenu = tk.Menu(self, tearoff = 0)
        self.FileMenu.add_command(label="New")
        self.FileMenu.add_command(label="Open")
        self.FileMenu.add_command(label="Save")
        self.FileMenu.add_command(label="Save As...")
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit")
        self.add_cascade(label="File", menu=self.FileMenu)