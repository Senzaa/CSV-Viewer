import tkinter as tk

class AppWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("CSV Viewer")
        self.geometry("800x450")