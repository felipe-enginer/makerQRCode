import tkinter as tk
from src.gui import QRCodeApp

def main():
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
