import tkinter as tk
from tkinter import messagebox, ttk

root= tk.Tk()
root.title("Conversor de moedas")
root.geometry("300x150")
taxas = {
    "USD": 1.0,
    "BRL": 5.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.00
   }
label_valor = tk.Label(text="Valor")
label_valor.grid(row=0, column=0, padx=5,pady=5)

entry_valor=tk.Entry()
entry_valor.grid(row=0, column=1, sticky="ew")


moeda_o = tk.Label(text="Moeda de Origem")
moeda_o.grid(row=1, column=0, padx=10,pady=10)

combobox = ttk.Combobox(root, values = ["BRL", "USD", "EUR","GBP", "JPY"],state= "readnoly")
combobox.grid(row=1, column=1)

moeda_d = tk.Label(text="Moeda de Destino")
moeda_d.grid(row=2, column=0, padx=10,pady=10)

combobox2=ttk.Combobox(root, values = ["BRL", "USD", "EUR","GBP", "JPY"],state= "readnoly")
combobox2.grid(row=2, column=1, padx=10,pady=10)

def converter():
    try:    
        valor = float(entry_valor.get().replace(",", "."))
        moeda_origem= combobox.get()
        moeda_destino= combobox2.get()

    # Primeiro transforma o valor em USD
        valor_usd = valor / taxas[moeda_origem]
        resultado= valor_usd / taxas[moeda_destino]

        messagebox.showinfo(
        "Resultado",
        f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")


    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

button=tk.Button(text="Converter",command=converter)
button.grid(row=3,column=0, columnspan=2)
root.mainloop()

