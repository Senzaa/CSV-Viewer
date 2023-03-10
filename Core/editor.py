from tkinter.messagebox import showerror, showwarning, showinfo, askyesno, askokcancel, askyesnocancel
from tkinter import filedialog as fd
from Core.data import Spreadsheet
from os import path

class EditorData():
    slots = '__fileName', '__spreadsheet'
    def __init__(self, fileName, spreadsheet):
        self.__fileName = fileName
        self.__spreadsheet = spreadsheet
    
    @property
    def Filename(self) -> str:
        return self.__fileName
    
    @Filename.setter
    def Filename(self, val: str):
        self.__fileName = val or 'unknown.csv'
    
    @property
    def Spreadsheet(self) -> Spreadsheet:
        return self.__spreadsheet

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

    def LoadData(self, file) -> Spreadsheet:
        if path.exists(file):
            self.__currentData = EditorData(file, Spreadsheet.from_csv(file))
        return self.__currentData
    
    def Save(self, file=None):
        if self.HasData:
            target = file or self.__currentData.Filename
            if target != None:
                self.__currentData.Spreadsheet.to_csv(target)
            else:
                self.SaveAsDialog()
    
    def NewEmpty(self):
        if self.HasData:
            result = askyesnocancel('Warning!', 'Save changes before creating a new CSV file?')
            if result == True:
                self.Save()
            elif result == None:
                return
        self.__currentData = EditorData(None, Spreadsheet())

    def OpenDialog(self):
        if self.HasData:
            result = askyesnocancel('Warning!', 'Save changes before opening?')
            if result == True:
                if self.CurrentData.Filename != None:
                    self.Save()
                else:
                    self.SaveAsDialog()
            elif result == None:
                return
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
