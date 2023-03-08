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
    
    def AskOpenFile(self):
        fileName = None
        try:
            fileName = fd.askopenfile(
                filetypes = (
                    ("CSV files", "*.csv"),
                    ("All files", "*.*")
                )
            ).name
        except Exception as ex:
            showerror(title="Error", message=str(ex))
        return fileName

    
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
    
    def Save(self, file):
        if self.HasData:
            self.__currentData["DataFrame"].to_csv(file or self.__currentData["Filename"], sep="\t", encoding="utf-8")
    
    def SaveTo(self):
        if self.HasData:
            self.Save(
                fd.asksaveasfile(
                    initialfile=path.basename(self.__currentData["Filename"]),
                    defaultextension=".csv",
                    filetypes = (
                        ("CSV files", "*.csv"),
                        ("All files", "*.*")
                    )
                ).name
            )
