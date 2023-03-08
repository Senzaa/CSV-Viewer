from Core.editor import Editor
Editor_Instance = Editor()
from UI.uimain import UIManager
UIManager_Instance = UIManager()

def main():
    UIManager_Instance.run()

if __name__ == "__main__":
    main()