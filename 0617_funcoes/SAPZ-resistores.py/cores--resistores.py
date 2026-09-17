import tkinter as tk
from tkinter import ttk,Canvas

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.geometry("800x400")
#janela.resizable(False, False)


CORES =[
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


combo1 = ttk.Combobox(janela, values = CORES, state="readonly") #Combobox banda 1
combo1.grid(row=0, column=1, sticky="w")

tk.Label(janela, text="Banda 1").grid(row=0, column=0,sticky="e" ) #Texto banda 1

combo2 = ttk.Combobox(janela, values=CORES, state="readonly") # Combobox banda 2
combo2.grid(row=1, column=1,sticky="w")
tk.Label(janela, text="Banda 2").grid(row=1, column=0,sticky="e") #Texto banda 2


combo3 = ttk.Combobox(janela, values=CORES, state="readonly") #Combobox banda 3
combo3.grid(row=2, column=1, sticky="w")
tk.Label(janela, text="Banda 3").grid(row=2, column=0,sticky="e") #Texto banda 3


combo4 = ttk.Combobox(janela, values=cores_tolerancia, state="readonly") #Combobox tolerância
combo4.grid(row=3, column=1, sticky="w")
tk.Label(janela, text="Tolerância").grid(row=3, column=0,sticky="e") #Texto tolerância

#tk.Label(
#    janela,
#    text="Digite a resistência (Ω):"
#).grid(row=0, column=2, padx=20, sticky="e")

#entrada_resistencia = tk.Entry(janela, width=15)
#entrada_resistencia.grid(row=0, column=4, sticky="w")

frame_valor = tk.LabelFrame(janela, text="Valor -> para cores", padx=10, pady=10)
frame_valor.grid(row=0, column=2, rowspan=4, padx=20, pady=5, sticky="n")

tk.Label(frame_valor, text="Resistência:").grid(row=0, column=0, sticky="e")
entrada_resistencia = tk.Entry(frame_valor, width=10)
entrada_resistencia.grid(row=0, column=1, padx=5)

unidade_var = tk.StringVar(value="Ω")
combo_unidade = ttk.Combobox(
    frame_valor, textvariable=unidade_var,
    values=["Ω", "KΩ", "MΩ"], state="readonly", width=5
)
combo_unidade.grid(row=0, column=2, padx=5)



def faixa1(cor):#Aqui é o valor de cada cor
    
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

def faixa2(cor): #Aqui é o valor de cada cor

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
    
    
def multiplicador(cor): # Aqui é os multiplicadores de acordo com as cores
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



def tolerancia(cor): # Aqui é a tolerancia e seus valores

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




canvas = tk.Canvas(    #Cria a janela para desnho do resistor
    janela,
    width=600,
    height=200,
    bg="white"
)

canvas.grid(    # Mostra a janela de desenho na janela do tkinter
    row=6,
    column=0,
    columnspan=2,
    pady=20
)



def calcular():
    cor1 = combo1.get() # cor1, cor2... são variaveis para os combobox
    cor2 = combo2.get()
    cor3 = combo3.get()
    cor4 = combo4.get()

    numero = faixa1(cor1) * 10 + faixa2(cor2)    #primeira parte do calculo
    resistencia = numero * multiplicador(cor3)
    tol = tolerancia(cor4)

    minimo = resistencia -(resistencia * tol /100)  #minimo e maximo de resistencia de acordo com a tolerancia
    maximo = resistencia +(resistencia * tol /100)

    resultado.config(
    text=f"Resistência: {escalas(resistencia)}  ±{tol}%\n" #Exebição de qual é a resistencia e qual seu valor minimo e maximo de acordo com a faixa de tolerancia
         f"Mínimo: {escalas(minimo)} \n"
         f"Máximo: {escalas(maximo)} ")
    resistor(cor1, cor2, cor3, cor4)
    
    

def faixa_resistor(cor):   #ja que o tkinter trabalha com as cores em ingles, aqui é passado do portugues para ingles
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



    canvas.create_text(190, 150, text=cor1, font=("Arial", 8 )) #Mostra o nome da cor escolhida, abaixo de respectiva cor
    canvas.create_text(240, 150, text=cor2, font=("Arial", 8 ))
    canvas.create_text(290, 150, text=cor3, font=("Arial", 8 ))
    canvas.create_text(385, 150, text=cor4, font=("Arial", 8 ))
                    
def escalas(ohms):     #transforma os ohms de forma compactada em vez de escrever 1000000 de ohms podemos escrever 1M ohms
    if ohms >= 1_000_000:
        return f"{ohms / 1_000_000:g} MΩ"
    if ohms >= 1_000:
        return f"{ohms / 1_000:g} kΩ"
    return f"{ohms:g} Ω"

def valor_para_cores():
    try:
        valor = float(entrada_resistencia.get())
        unidade = unidade_var.get()
        fator_unidade = {"Ω": 1, "kΩ": 1_000, "MΩ": 1_000_000}[unidade]
        valor *= fator_unidade

        if valor <= 0:
            raise ValueError

        encontrado = None

        for multiplicador, dados in CORES.items():
            fator = dados[1]
            if fator and valor / fator >= 10 and valor / fator <= 99: #testa se o valor dividido tem dois digitos entre 10 e 99
                numero = valor / fator #atribui o valor dividido a variavel
                if numero.is_integer(): #valida se é um inteiro
                    numero = int(numero)
                    faixa1, faixa2 = numero // 10, numero % 10
                    encontrado = [faixa1, faixa2, multiplicador] #atribui os digitos a variavel encontrado.
                    break

        if not encontrado:
            resultado.config(text="Valor não representável") #se o valor não for represntavel retorna o erro
        
            return

        tolerancia = combo4.get() #pega a tolerancia selecionada no combobox
        resultado.config(text=f"{escalas(valor)} ± {CORES[tolerancia][3]}%") #exibe o valor formatado com a tolerância
        combo1.set(encontrado[0])
        combo2.set(encontrado[1])
        combo3.set(encontrado[2])
        resistor(encontrado + [tolerancia]) #chama a função desenhar passando as cores encontradas e a tolerancia selecionada

    except:
        resultado.config(text="Digite um valor válido")


resistor()
botao = tk.Button(janela, text="Calcular resistência", command= calcular) #cria o botão de calcular o resistores escolhendo as cores
botao.grid(row= 4, column=1, sticky="w")
#numero = faixa1 * 10 + faixa2
#resistencia = numero * multiplicador

btn_converter = tk.Button(frame_valor, text="Converter", command=valor_para_cores)
btn_converter.grid(row=1, column=0, columnspan=3, pady=10)







janela.mainloop()