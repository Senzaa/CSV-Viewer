import tkinter as tk

class GridContextMenu(tk.Menu):
    slots = '__selectedRow', '__selectedColumn'
    def __init__(self, master, datagrid):
        tk.Menu.__init__(self, master)
        self.configure(tearoff=0)
        self.add_command(label='Add column before', command=lambda: datagrid.InsertColumn(self.__selectedColumn))
        self.add_command(label='Add column after', command=lambda: datagrid.InsertColumn(self.__selectedColumn+1))
        self.add_command(label='Delete entire column', command=lambda: datagrid.RemoveColumn(self.__selectedColumn))

        self.add_command(label='Add row above', command=lambda: datagrid.InsertRow(self.__selectedRow))
        self.add_command(label='Add row below', command=lambda: datagrid.InsertRow(self.__selectedRow+1))
        self.add_command(label='Delete entire row', command=lambda: datagrid.RemoveRow(self.__selectedRow))
    
    def tk_popup(self, x: int, y: int, row: int, col: int, entry: str | int = "") -> None:
        self.__selectedRow = row
        self.__selectedColumn = col
        return super().tk_popup(x, y, entry)
        