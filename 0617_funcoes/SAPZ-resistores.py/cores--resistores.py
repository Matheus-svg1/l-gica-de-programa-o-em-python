import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.geometry("800x600")

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

 
combo1 = ttk.Combobox(janela, values = cores, state="readonly")
combo1.pack(pady = 5)

tbanda1 = tk.Label(janela, text = "banda 1")
tbanda1.pack( sticky='w')

combo2 = ttk.Combobox(janela, values = cores, state="readonly")
combo2.pack(pady = 5)

combo3 = ttk.Combobox(janela, values = cores, state="readonly")
combo3.pack(pady = 5)
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
    pass
    
    
    

#numero = faixa1 * 10 + faixa2
#resistencia = numero * multiplicador


janela.mainloop()