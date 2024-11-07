# main.py
import tkinter as tk
from ui import ContactManagerApp
from db import init_db

def main():
    init_db()
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
