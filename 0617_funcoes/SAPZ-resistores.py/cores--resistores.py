import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.geometry("700x500")

cores =[
    "preto",
    "marrom",
    "vermelho",
    "laranja",
    "amarelo",
    "verde",
    "azul",
    "violeta",
    "cinza",
    "branco",
]

cores_tolerancia =[
    "marrom",
    "vermelho",
    "verde",
    "azul",
    "violeta",
    "cinza",
    "dourado",
    "prata",
]
combo1 = ttk.Combobox(janela, values = cores, state="readonly") #Combobox banda 1
combo1.grid(row=0, column=1)

tk.Label(janela, text="Banda 1").grid(row=0, column=0, sticky="w") #Texto banda 1
#tbanda1 = tk.Label(janela, text = "banda 1")
#tbanda1.pack(anchor = "w")

combo2 = ttk.Combobox(janela, values=cores, state="readonly") # Combobox banda 2
combo2.grid(row=1, column=1)
tk.Label(janela, text="Banda 2").grid(row=1, column=0, sticky="w") #Texto banda 2


combo3 = ttk.Combobox(janela, values=cores, state="readonly") #Combobox banda 3
combo3.grid(row=2, column=1)
tk.Label(janela, text="Banda 3").grid(row=2, column=0, sticky="w") #Texto banda 3


combo4 = ttk.Combobox(janela, values=cores_tolerancia, state="readonly") #Combobox tolerância
combo4.grid(row=3, column=1)
tk.Label(janela, text="Tolerância").grid(row=3, column=0, sticky="w") #Texto tolerância





def faixa1(cor):
    
    if cor == "preto":
        return 0
    elif cor == "marrom":
        return 1
    elif cor == "vermelho": 
        return 2
    elif cor == "laranja":
        return 3
    elif cor == "amarelo":
        return 4
    elif cor == "verde":
        return 5
    elif cor == "azul":
        return 6
    elif cor == "violeta":
        return 7
    elif cor == "cinza":
        return 8
    elif cor == "branco":
        return 9
    else:
        print("Escolha uma opção válida!")

def faixa2(cor):

    if cor == "preto":
        return 0
    elif cor == "marrom":
        return 1
    elif cor == "vermelho": 
        return 2
    elif cor == "laranja":
        return 3
    elif cor == "amarelo":
        return 4
    elif cor == "verde":
        return 5
    elif cor == "azul":
        return 6
    elif cor == "violeta":
        return 7
    elif cor == "cinza":
        return 8
    elif cor == "branco":
        return 9
    else:
        print("Escolha uma opção válida!")
    
    
def multiplicador(cor):
    if cor == "preto":
        return 1
    elif cor == "marrom":
        return 10
    elif cor == "vermelho": 
        return 100
    elif cor == "laranja":
        return 1000
    elif cor == "amarelo":
        return 10000
    elif cor == "verde":
        return 100000
    elif cor == "azul":
        return 1000000
    elif cor == "violeta":
        return 10000000
    elif cor == "cinza":
        return 100000000
    elif cor == "branco":
        return 100000000
    else:
        print("Escolha uma opção válida!")



def tolerancia(cor):

    if cor == "marrom":
        return 1
    elif cor == "vermelho": 
        return 2
    elif cor == "verde":
        return 0.5
    elif cor == "azul":
        return 0.25
    elif cor == "violeta":
        return 0.1
    elif cor == "cinza":
        return 0.05
    elif cor == "dourado":
        return 5
    elif cor == "prata":
        return 10
    
    
def calcular():
    cor1 = combo1.get()
    cor2 = combo2.get()
    cor3 = combo3.get()
    cor4 = combo4.get()

    numero = faixa1(cor1) * 10 + faixa2(cor2)
    resistencia = numero * multiplicador(cor3)
    tol = tolerancia

    minimo = resistencia -(resistencia * tol /100)
    maximo = resistencia +(resistencia * tol /100)

botao = tk.Button(janela, text="Calcular resistência", command= calcular)
botao.grid(row= 4, column=1,)



#numero = faixa1 * 10 + faixa2
#resistencia = numero * multiplicador


janela.mainloop()