import tkinter as tk
from instance import Editor_Instance

class TopMenu(tk.Menu):
    slots = 'FileMenu', 'EditMenu'
    def __init__(self, master, datagrid):
        tk.Menu.__init__(self, master)

        def applyAndFire(target):
            datagrid.CommitChanges()
            target()

        def fireAndUpdate(target):
            target()
            datagrid.FillDatagrid()

        # File Menu
        self.FileMenu = tk.Menu(self, tearoff = 0)
        self.FileMenu.add_command(label="New", underline=0, accelerator="Ctrl+N", command=(lambda: fireAndUpdate(Editor_Instance.NewEmpty)))
        self.FileMenu.add_command(label="Open", underline=0, accelerator="Ctrl+O", command=(lambda: fireAndUpdate(Editor_Instance.OpenDialog)))
        self.FileMenu.add_command(label="Save", underline=0, accelerator="Ctrl+S", command=(lambda: applyAndFire(Editor_Instance.Save)))
        self.FileMenu.add_command(label="Save As...", underline=0, accelerator="Ctrl+Shift+S", command=(lambda: applyAndFire(Editor_Instance.SaveAsDialog)))
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit")
        self.add_cascade(label="File", menu=self.FileMenu)

        # Edit Menu
        self.EditMenu = tk.Menu(self, tearoff = 0)
        self.EditMenu.add_command(label="Search keyword", accelerator="Ctrl+F")
        self.add_cascade(label="Edit", menu=self.EditMenu)