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

        peso = float(entry1.get())
        altura = float(entry2.get())

        imc = peso / (altura ** 2)

        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif imc < 25:
            situacao = "Peso ideal"
        elif imc < 30:
            situacao = "Sobrepeso"
        elif imc < 35:
            situacao = "Obesidade Grau I"
        elif imc < 40:
            situacao = "Obesidade Grau II"
        else:
            situacao = "Obesidade Grau III"

        messagebox.showinfo(
            "Resultado",
            f"Seu IMC é {imc:.2f}\nClassificação: {situacao}"
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