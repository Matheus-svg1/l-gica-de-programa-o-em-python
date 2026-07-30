import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

spinbox_Var = tk.StringVar(value = "0")    #StringVar é uma variável que armazena uma string
                                           #é usada para atus
spinbox = tk.Spinbox(root,
    from_=-10,
    to = 10,
    #increment = 5,
    textvariable = spinbox_Var)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable = spinbox_Var)
label.pack()


root.mainloop()