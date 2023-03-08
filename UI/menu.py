import tkinter as tk
from instance import Editor_Instance

class TopMenu(tk.Menu):
    slots = 'FileMenu', 'EditMenu'
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        # File Menu
        self.FileMenu = tk.Menu(self, tearoff = 0)
        self.FileMenu.add_command(label="New", underline=0, accelerator="Ctrl+N", command=Editor_Instance.NewEmpty)
        self.FileMenu.add_command(label="Open", underline=0, accelerator="Ctrl+O", command=Editor_Instance.OpenDialog)
        self.FileMenu.add_command(label="Save", underline=0, accelerator="Ctrl+S", command=Editor_Instance.Save)
        self.FileMenu.add_command(label="Save As...", underline=0, accelerator="Ctrl+Shift+S", command=Editor_Instance.SaveAsDialog)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit")
        self.add_cascade(label="File", menu=self.FileMenu)

        # Edit Menu
        self.EditMenu = tk.Menu(self, tearoff = 0)
        self.EditMenu.add_command(label="Search keyword", underline=1, accelerator="Ctrl+F")
        self.add_cascade(label="Edit", menu=self.EditMenu)