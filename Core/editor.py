from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import filedialog as fd
import pandas as pd
from os import path

class Editor():
    slots = '__currentData'
    def __init__(self):
        self.__currentData = None

    def CurrentData(self):
        return self.__currentData
    
    @property
    def HasData(self):
        return self.__currentData != None

    def LoadData(self, file) -> pd.DataFrame:
        if self.HasData:
            self.Save()
        if path.exists(file):
            self.__currentData = {
                "Filename": file,
                "DataFrame": pd.read_csv(file)
            }
        return self.GetData()
    
    def GetData(self) -> pd.DataFrame:
        return self.__currentData["DataFrame"]
    
    def Save(self, file=None):
        if self.HasData:
            target = file or self.__currentData["Filename"]
            if target != None:
                self.__currentData["DataFrame"].to_csv(target, sep="\t", encoding="utf-8")
            else:
                self.SaveAsDialog()
    
    def SetCellValue(self, row, col, data):
        if self.HasData:
            df: pd.DataFrame = self.__currentData["DataFrame"]
            df.at[row, col] = data
    
    def GetCellValue(self, row, col):
        if self.HasData:
            return self.__currentData["DataFrame"].at[row, col]

    def NewEmpty(self):
        self.Save()
        self.__curentData = {
            "Filename": None,
            "DataFrame": pd.DataFrame()
        }

    def OpenDialog(self):
        target = fd.askopenfile(
            filetypes = (
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            )
        )
        self.LoadData(
            
        )

    def SaveAsDialog(self):
        if self.HasData:
            target = fd.asksaveasfile(
                initialfile=path.basename(self.__currentData["Filename"]),
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
        else:
            target = fd.asksaveasfile(
                initialfile="My New CSV Spreadsheet",
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
