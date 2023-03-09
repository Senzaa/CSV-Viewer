import tkinter as tk
from tkinter import ttk
import pandas as pd
from instance import Editor_Instance

class DataCell(tk.Entry):
    slots = '_row', '_column'
    def __init__(self, row, column, **kvargs):
        tk.Entry.__init__(self, **kvargs)
        self._row = row
        self._column = column
        self.grid(row=row, column=column)

class DataGrid(ttk.Frame):
    slots = '__datagrid'
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack(padx=5, pady=5)
        self.__datagrid = []
    
    @property
    def df(self) -> pd.DataFrame:
        return Editor_Instance.CurrentData.DataFrame
    
    def FillDatagrid(self):
        print("Filling datagrid")
        rowsCount, columnsCount = len(self.df.index), len(self.df.columns)

        for row in range(max(10, rowsCount)):
            if len(self.__datagrid) <= row:
                self.__datagrid.append([])
            for column in range(max(10, columnsCount)):
                if len(self.__datagrid[row]) <= column:
                    strVar = tk.StringVar()
                    ent = tk.Entry(self, justify = tk.CENTER, width = 10, textvariable=strVar)
                    ent.grid(row=row, column=column)
                    self.__datagrid[row].append(strVar)
                if column < columnsCount and row < rowsCount:
                    self.__datagrid[row][column].set(self.df.iat[row, column])
                else:
                    self.__datagrid[row][column].set('')
    
    def CommitChanges(self):
        print("Comitting changes")
        rowsCount, columnsCount = len(self.df.index), len(self.df.columns)
        for row in range(len(self.__datagrid)):
            for column in range(len(self.__datagrid[row])):
                if column < columnsCount and row < rowsCount:
                    self.df.iat[row, column] = self.__datagrid[row][column].get()

    def InsertRow(self, data, at = -1):
        self.df.loc[at] = data
        self.FillDatagrid()
    
    def RemoveRow(self, index: int):
        self.df.drop(index)
        self.FillDatagrid()

    def InsertColumn(self, column, value = None, at = -1):
        self.df.insert(at, column, value)
        self.FillDatagrid()
    
    def RemoveColumn(self, column):
        self.df.drop(column, axis=1)
        self.FillDatagrid()