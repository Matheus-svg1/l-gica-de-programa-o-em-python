import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("SENAI - Sistemas")

label1 = tk.Label(root, text= "Peso(kg)")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text= "Altura(m)")
entry2 = tk.Entry(root)

def imc():
 label2*label2 / label1 = imc
def button_command():
    messagebox.showinfo(f"Resultado", "Seu IMC é {imc}"
    )
button = tk.Button(
        root,
        text = "Calcular",
        command = button_command
)


















label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

button.pack()
root.mainloop()