import tkinter as tk
from tkinter import ttk
from ui import AuthWindow

root = tk.Tk()
root.title("Bienvenido")

auth_window = AuthWindow(root)
auth_window.pack()

root.mainloop()
