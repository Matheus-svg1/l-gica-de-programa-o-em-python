import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def enter_pressionado(event):
    label.config(text=event.widget.get())

entry = tk.Entry(root)
entry.insert(0, "Digite seu texto")
entry.bind("<Return>", enter_pressionado)# o <Return> 
entry.pack()

label = tk.Label(root, text = "Demonstração!")
label.pack()
root.mainloop()