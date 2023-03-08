from tkinter.messagebox import showerror, showwarning, showinfo, askyesno, askokcancel, askyesnocancel
from tkinter import filedialog as fd
import pandas as pd
from os import path

class EditorData():
    slots = '__fileName', '__dataFrame'
    def __init__(self, fileName, dataFrame):
        self.__fileName = fileName
        self.__dataFrame = dataFrame
    
    @property
    def Filename(self) -> str:
        return self.__fileName
    
    @Filename.setter
    def Filename(self, val: str):
        self.__fileName = val or 'unknown.csv'
    
    @property
    def DataFrame(self) -> pd.DataFrame:
        return self.__dataFrame

class Editor():
    slots = '__currentData'
    def __init__(self):
        self.__currentData = None

    @property
    def CurrentData(self) -> EditorData:
        return self.__currentData
    
    @property
    def HasData(self):
        return self.__currentData != None

    def LoadData(self, file) -> pd.DataFrame:
        if self.HasData:
            if askokcancel('Warning!', 'Save changes before opening?'):
                self.Save()
        if path.exists(file):
            self.__currentData = EditorData(file, pd.read_csv(file, sep=",", header=None, encoding="utf-8"))
        return self.GetData()
    
    def GetData(self) -> EditorData:
        return self.__currentData
    
    def Save(self, file=None):
        if self.HasData:
            target = file or self.__currentData.Filename
            if target != None:
                self.__currentData.DataFrame.to_csv(target, sep=",", header=None, index = False, encoding="utf-8")
            else:
                self.SaveAsDialog()
    
    def SetCellValue(self, row, col, data):
        if self.HasData:
            df: pd.DataFrame = self.__currentData.DataFrame
            df.at[row, col] = data
    
    def GetCellValue(self, row, col):
        if self.HasData:
            return self.__currentData.DataFrame.at[row, col]

    def NewEmpty(self):
        if self.HasData:
            result = askyesnocancel('Warning!', 'Save changes before creating a new CSV file?')
            if result == True:
                self.Save()
            elif result == None:
                return
        self.__currentData = EditorData(None, pd.DataFrame())

    def OpenDialog(self):
        target = fd.askopenfile(
            filetypes = (
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            )
        )
        if target:
            self.LoadData(
                target.name
            )

    def SaveAsDialog(self):
        target = fd.asksaveasfile(
            title = 'Save As...',
            initialfile=path.basename((self.HasData and self.__currentData.Filename != None) and self.__currentData.Filename or 'new.csv'),
            defaultextension=".csv",
            filetypes = (
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            )
        )
        if target:
            self.Save(
                target.name
            )
            if self.HasData:
                self.__currentData.Filename = target.name
            else:
                self.LoadData(target.name)
