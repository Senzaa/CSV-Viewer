from UI.window import AppWindow

class UIManager():
    slots = '__appWindow'
    def __init__(self):
        self.__appWindow = AppWindow()
    
    def run(self):
        self.__appWindow.mainloop()