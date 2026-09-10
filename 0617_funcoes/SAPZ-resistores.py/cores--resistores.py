import tkinter as tk
from tkinter import ttk,Canvas

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
combo1.grid(row=0, column=1, sticky ="w")

tk.Label(janela, text="Banda 1").grid(row=0, column=0, sticky="e") #Texto banda 1
#tbanda1 = tk.Label(janela, text = "banda 1")
#tbanda1.pack(anchor = "w")

combo2 = ttk.Combobox(janela, values=cores, state="readonly") # Combobox banda 2
combo2.grid(row=1, column=1, sticky ="w")
tk.Label(janela, text="Banda 2").grid(row=1, column=0, sticky="e") #Texto banda 2


combo3 = ttk.Combobox(janela, values=cores, state="readonly") #Combobox banda 3
combo3.grid(row=2, column=1, sticky ="w")
tk.Label(janela, text="Banda 3").grid(row=2, column=0, sticky="e") #Texto banda 3


combo4 = ttk.Combobox(janela, values=cores_tolerancia, state="readonly") #Combobox tolerância
combo4.grid(row=3, column=1, sticky ="w")
tk.Label(janela, text="Tolerância").grid(row=3, column=0, sticky="e") #Texto tolerância





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
        return 1000000000
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
    
resultado = tk.Label(janela, text="")
resultado.grid(row=5, column=0, columnspan=2)    




canvas = tk.Canvas(
    janela,
    width=600,
    height=200,
    bg="white"
)

canvas.grid(
    row=6,
    column=0,
    columnspan=2,
    pady=20
)



def calcular():
    cor1 = combo1.get()
    cor2 = combo2.get()
    cor3 = combo3.get()
    cor4 = combo4.get()

    numero = faixa1(cor1) * 10 + faixa2(cor2)
    resistencia = numero * multiplicador(cor3)
    tol = tolerancia(cor4)

    minimo = resistencia -(resistencia * tol /100)
    maximo = resistencia +(resistencia * tol /100)

    resultado.config(
    text=f"Resistência: {resistencia} Ω ±{tol}%\n"
         f"Mínimo: {minimo} Ω\n"
         f"Máximo: {maximo} Ω")
    resistor(cor1, cor2, cor3, cor4)
    
    

def faixa_resistor(cor):
    if cor =="preto":
        return "black"
    elif cor == "marrom":
        return "brown"
    elif cor == "vermelho": 
        return "red"
    elif cor == "laranja":
        return "orange"
    elif cor == "amarelo":
        return "yellow"
    elif cor == "verde":
        return "green"
    elif cor == "azul":
        return "blue"
    elif cor == "violeta":
        return "violet"
    elif cor == "cinza":
        return "gray"
    elif cor == "branco":
        return "white"
    elif cor == "dourado":
        return "gold"
    elif cor == "prata":
        return "silver"

def resistor(cor1="",cor2="",cor3="",cor4=""):
    canvas.delete("all")

    # fio esquerdo
    canvas.create_line(
        50, 100,
        150, 100,
        width=5
    )

    # corpo do resistor
    canvas.create_rectangle(
        150, 70,
        450, 130,
        fill="beige",
        outline="black"
    )

    # fio direito
    canvas.create_line(
        450, 100,
        550, 100,
        width=5
    )
    canvas.create_rectangle(180, 70, 200, 130,fill=faixa_resistor(cor1)) #Faixas do resistor

    canvas.create_rectangle(230, 70, 250, 130,fill=faixa_resistor(cor2)) #Faixas do resistor

    canvas.create_rectangle(280, 70, 300, 130, fill=faixa_resistor(cor3)) #Faixas do resistor

    canvas.create_rectangle(375, 70, 400, 130,fill=faixa_resistor(cor4)) #Faixas do resistor



    canvas.create_text(190, 150, text=cor1, font=("Arial", 9, "bold"))
    canvas.create_text(240, 150, text=cor2, font=("Arial", 9, "bold"))
    canvas.create_text(290, 150, text=cor3, font=("Arial", 9, "bold"))
    canvas.create_text(460, 400, text=cor4, font=("Arial", 9, "bold"))
                    

resistor()
botao = tk.Button(janela, text="Calcular resistência", command= calcular)
botao.grid(row= 4, column=1, sticky="w")
#numero = faixa1 * 10 + faixa2
#resistencia = numero * multiplicador







janela.mainloop()