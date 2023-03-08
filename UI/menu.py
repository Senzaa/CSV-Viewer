import tkinter as tk

class TopMenu(tk.Menu):
    slots = 'FileMenu', 'EditMenu'
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        # File Menu
        self.FileMenu = tk.Menu(self, tearoff = 0)
        self.FileMenu.add_command(label="New", underline=0, accelerator="Ctrl+N")
        self.FileMenu.add_command(label="Open", underline=0, accelerator="Ctrl+O")
        self.FileMenu.add_command(label="Save", underline=0, accelerator="Ctrl+S")
        self.FileMenu.add_command(label="Save As...", underline=0, accelerator="Ctrl+Shift+S")
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit")
        self.add_cascade(label="File", menu=self.FileMenu)

        # Edit Menu
        self.EditMenu = tk.Menu(self, tearoff = 0)
        self.EditMenu.add_command(label="Search keyword", underline=1, accelerator="Ctrl+F")
        self.add_cascade(label="Edit", menu=self.EditMenu)