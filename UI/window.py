import tkinter as tk
from UI.menu import TopMenu
from UI.datagrid import DataGrid

class AppWindow(tk.Tk):
    slots = '__topMenu', '__dataGrid'
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("CSV Viewer")
        self.geometry("800x450")

        self.__dataGrid = DataGrid(self)
        self.__topMenu = TopMenu(self, self.__dataGrid)

        self.config(menu=self.__topMenu)