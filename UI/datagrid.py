import tkinter as tk
from Core.data import Spreadsheet
from tkinter import ttk
from instance import Editor_Instance
from UI.gridmenu import GridContextMenu

class DataGrid(ttk.Frame):
    slots = '__datagrid', '__gridContextMenu'
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(padx=5, pady=5)
        self.__datagrid = []
        self.__gridContextMenu = GridContextMenu(master, self)
    
    @property
    def st(self) -> Spreadsheet:
        return Editor_Instance.CurrentData.Spreadsheet
    
    def FillDatagrid(self):
        if not Editor_Instance.HasData:
            print("No data provided to fill datagrid with.")
            return

        def contextHandler(event, row, column):
            print(row, column)
            self.__gridContextMenu.tk_popup(event.x_root, event.y_root, row, column)
        for row in range(self.st.rowsCount):
            if len(self.__datagrid) <= row:
                self.__datagrid.append([])
            for column in range(self.st.columnsCount):
                if len(self.__datagrid[row]) <= column:
                    strVar = tk.StringVar()
                    ent = tk.Entry(self, justify = tk.CENTER, width = 10, textvariable=strVar)
                    ent.grid(row=row, column=column)
                    bindId = ent.bind("<Button-3>", lambda event, r=row, c=column: contextHandler(event, r, c))
                    self.__datagrid[row].append((strVar, bindId, ent))
                self.__datagrid[row][column][0].set(self.st[row, column])
    
    def CommitChanges(self):
        if not Editor_Instance.HasData:
            print("No data provided to commit changes to.")
            return
        for row in range(self.st.rowsCount):
            for column in range(self.st.columnsCount):
                self.st[row, column] = self.__datagrid[row][column][0].get()

    def InsertRow(self, index: int):
        self.CommitChanges()
        if index < self.st.rowsCount:
            self.st.insertRow(index)
        else:
            self.st.appendRow()
        self.FillDatagrid()
    
    def RemoveRow(self, index: int):
        self.CommitChanges()
        for row in range(self.st.rowsCount):
            if row == index:
                for column in range(self.st.columnsCount):
                    data: tuple[tk.StringVar, str, tk.Entry] = self.__datagrid[row][column]
                    data[2].unbind(data[1])
                    data[2].grid_forget()
                self.__datagrid.pop(row)
                break
        self.st.removeRow(index)
        self.FillDatagrid()

    def InsertColumn(self, index: int):
        self.CommitChanges()
        if index < self.st.columnsCount:
            self.st.insertColumn(index, '')
        else:
            self.st.appendColumn('')
        self.FillDatagrid()
    
    def RemoveColumn(self, index: int):
        self.CommitChanges()
        for row in range(self.st.rowsCount):
            for column in range(self.st.columnsCount):
                if column == index:
                    data: tuple[tk.StringVar, str, tk.Entry] = self.__datagrid[row][column]
                    data[2].unbind(data[1])
                    data[2].grid_forget()
                    self.__datagrid[row].pop(column)
                    break
        self.st.removeColumn(index)
        self.FillDatagrid()