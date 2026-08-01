import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("SENAI - Sistemas")

root.geometry("600x600")

label1 = tk.Label(root, text= "Peso(kg)")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text= "Altura(m)")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="")


def button_command():
    try:
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

    except ValueError:
        label3.config(text="Informe valores válidos")


        label3.config(text=situacao)

        messagebox.showinfo(
            "Resultado",
            f"Seu IMC é {imc:.2f}")
            
        

    

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

label3.pack()

root.mainloop()