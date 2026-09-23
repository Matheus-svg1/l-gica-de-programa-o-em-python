import tkinter as tk
from tkinter import ttk, Canvas

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.geometry("800x650")

CORES = [         #lista das cores em suas posições
    "preto",
    "marrom",
    "vermelho",
    "laranja",
    "amarelo",
    "verde", 
    "azul",
    "violeta",
    "cinza",
    "branco"
]

cores_tolerancia = [     # lista das cores de tolerância em suas posições
    "marrom",
    "vermelho",
    "verde",
    "azul",
    "violeta",
    "cinza",
    "dourado",
    "prata"
]

# dicionários
VALORES = {cor: index for index, cor in enumerate(CORES)} # o enumerate vai pegar as posições das cores dentro do dicionário CORES ex: (0, "marrom"), (1,"vermelho")...
                                                           # o index guarda o numero da posição
MULTIPLICADORES = {
    "preto": 1, "marrom": 10, "vermelho": 100, "laranja": 1_000,
    "amarelo": 10_000, "verde": 100_000, "azul": 1_000_000,    # dicionário dos multiplicadores e o valor no qual cada cor multiplica
    "violeta": 10_000_000, "cinza": 100_000_000, "branco": 1_000_000_000
}

TOLERANCIA = {                                          # Tolerâncias dos resistores e suas respectivas variações em porcentagem (%)
    "marrom": 1, "vermelho": 2, "verde": 0.5, "azul": 0.25,
    "violeta": 0.1, "cinza": 0.05, "dourado": 5, "prata": 10
}


tk.Label(janela, text="Faixa 1").grid(row=0, column=0, sticky="e", padx=5, pady=2) # texto faixa 1
combo1 = ttk.Combobox(janela, values=CORES, state="readonly") # combobox faixa 1
combo1.grid(row=0, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Faixa 2").grid(row=1, column=0, sticky="e", padx=5, pady=2) # texto faixa 2
combo2 = ttk.Combobox(janela, values=CORES, state="readonly") # combobox faixa 2
combo2.grid(row=1, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Faixa 3").grid(row=2, column=0, sticky="e", padx=5, pady=2) # texto faixa 3
combo3 = ttk.Combobox(janela, values=CORES, state="readonly") # combobox faixa 3
combo3.grid(row=2, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Tolerância").grid(row=3, column=0, sticky="e", padx=5, pady=2) # texto tolerância
combo4 = ttk.Combobox(janela, values=cores_tolerancia, state="readonly") # combobox tolerância
combo4.grid(row=3, column=1, sticky="w", padx=5, pady=2)


frame_valor = tk.LabelFrame(janela, text="Valor -> para cores", padx=10, pady=10) # Cria uma janela(frame) dentro da janela do tkinter
frame_valor.grid(row=0, column=2, rowspan=4, padx=20, pady=5, sticky="n")

tk.Label(frame_valor, text="Resistência:").grid(row=0, column=0, sticky="e") # texto de resistência
entrada_resistencia = tk.Entry(frame_valor, width=10) # Entry para digitar a resistência
entrada_resistencia.grid(row=0, column=1, padx=5)

unidade_var = tk.StringVar(value="Ω")     # guarda a variável para não atrapalhar no código
combo_unidade = ttk.Combobox(                 # Combobox para a escolha da escala de resistência
    frame_valor, textvariable=unidade_var,
    values=["Ω", "KΩ", "MΩ","GΩ"], state="readonly", width=5
)
combo_unidade.grid(row=0, column=2, padx=5)



def faixa_resistor_hex(cor):
    
    hex_dic = {                 # dicionário de cores em formato Hexadecimal (#HEX)
        "preto": "#000000",
        "marrom": "#72370C",
        "vermelho": "#FF0000",
        "laranja": "#FFA500",
        "amarelo": "#FFFF00",
        "verde": "#008000",
        "azul": "#0000FF",
        "violeta": "#8A2BE2",
        "cinza": "#808080",
        "branco": "#FFFFFF",
        "dourado": "#D4AF37",
        "prata": "#C0C0C0"
    }
    return hex_dic.get(cor, "#D6AD78")  # retorna cor bege padrão caso não encontre


def escalas(ohms):  #formatação dos ohms para facilitar a leitura
    if ohms >= 1_000_000_000:
        return f"{ohms / 1_000_000_000}GΩ" 
    if ohms >= 1_000_000:
        return f"{ohms / 1_000_000:g} MΩ"
    if ohms >= 1_000:
        return f"{ohms / 1_000:g} kΩ"
    
    return f"{ohms:g} Ω"


def resistor(cor1="", cor2="", cor3="", cor4=""):
    canvas.delete("all")

    # fios do resistor
    canvas.create_line(50, 100, 150, 100, width=5, fill="black") # fio esquerdo
    canvas.create_line(450, 100, 550, 100, width=5, fill="black") # fio direito

    # corpo do resistor
    canvas.create_rectangle(150, 70, 450, 130, fill="#D8B27F", outline="black")

    # cria as faixas coloridas do resistor
    if cor1: canvas.create_rectangle(180, 70, 200, 130, fill=faixa_resistor_hex(cor1), outline="black")
    if cor2: canvas.create_rectangle(230, 70, 250, 130, fill=faixa_resistor_hex(cor2), outline="black")
    if cor3: canvas.create_rectangle(280, 70, 300, 130, fill=faixa_resistor_hex(cor3), outline="black")
    if cor4: canvas.create_rectangle(375, 70, 400, 130, fill=faixa_resistor_hex(cor4), outline="black")

    # textos em baixo de suas respectivas cores
    canvas.create_text(190, 150, text=cor1, font=("Arial", 8))
    canvas.create_text(240, 150, text=cor2, font=("Arial", 8))
    canvas.create_text(290, 150, text=cor3, font=("Arial", 8))
    canvas.create_text(385, 150, text=cor4, font=("Arial", 8))


# --- LÓGICA DE CÁLCULO ---
def calcular():
    cor1, cor2, cor3, cor4 = combo1.get(), combo2.get(), combo3.get(), combo4.get() # variáveis para os combobox

    if not (cor1 and cor2 and cor3 and cor4):      #verifica se todas as cores foram selecionadas
        resultado.config(text="Selecione todas as cores para calcular!")
        return

    numero = VALORES[cor1] * 10 + VALORES[cor2]  # junta os dois primeiros dígitos das cores (ex: 1 e 2 viram 12)
    resistencia = numero * MULTIPLICADORES[cor3] # cálculo da terceira faixa para obter o falor em ohms
    tol = TOLERANCIA[cor4] # tolerância

    minimo = resistencia - (resistencia * tol / 100) # valor mínimo de acordo com a variação da tolerância
    maximo = resistencia + (resistencia * tol / 100) # valor máximo de acordo com a variação da tolerância

    resultado.config( # configurando o resultado
        text=f"Resistência: {escalas(resistencia)}  ±{tol}%\n"
             f"Mínimo: {escalas(minimo)} | Máximo: {escalas(maximo)}"
    )
    resistor(cor1, cor2, cor3, cor4) # desenha o resistor por completo


def valor_para_cores():
    try:
        valor = float(entrada_resistencia.get()) # pega o valor digitado no campo de resistência
        unidade = unidade_var.get() # lê a unidade de medida selecionada no menu da tela (Ω, KΩ ou MΩ)
        fator_unidade = {"Ω": 1, "KΩ": 1_000, "MΩ": 1_000_000, "GΩ": 1_000_000_000}[unidade] # multiplica de acordo com a escala escolhida
        valor *= fator_unidade # pega a quantidade de ohms escolhida e multiplica de acordo com a sua escala

        if valor <= 0:
            resultado.config(text="Digite um valor maior que zero!") # verifica se foi digitado algum valor
            
            return

        encontrado = None

        for cor_mult, fator in MULTIPLICADORES.items():
            if fator > 0 and 10 <= (valor / fator) <= 99: # ele vai buscar no dicionario de multiplicadadores uma cor(fator, multiplicador) que encaixe entre 10 e 99
                numero = valor / fator # ele pega a resistencia e e fator que encaixou e faz a divisão
                if numero.is_integer(): # se o número for inteiro...
                    numero = int(numero)
                    d1, d2 = numero // 10, numero % 10 # pega o resultado da divisao anterior e o primeiro algarismo vira a primeira faixa do resistor e o resto da divisão vira a segunda faixa
                    cor1 = CORES[d1]
                    cor2 = CORES[d2]
                    encontrado = (cor1, cor2, cor_mult) # aqui foi encontrado a primera faixa, segunda e o multiplicador que deu origem nas duas faixas anteriores
                    break

        if not encontrado:
            resultado.config(text="Valor de resistência não padrão/representável!") # caso não encontre um valor válido
            return

        tolerancia_sel = combo4.get() or "dourado" # pega a tolerância escolhida ou define "dourado" 5% como padrão

        combo1.set(encontrado[0]) # busca a faixa 1 na posição 0 da variável encontrado
        combo2.set(encontrado[1]) # busca a faixa 2 na posição 1 da variável encontrado
        combo3.set(encontrado[2]) # busca a faixa 3 na posição 1 da variável encontrado
        combo4.set(tolerancia_sel) # busca a faixa 4 na vari´vel de tolerância selecionada

        tol_val = TOLERANCIA[tolerancia_sel] # bsucsa o valor da % da tolerância
        
        porcentagem = tol_val / 100 # transforma a porcentagem para a forma decimal ex: 5 -> 0.5
        minimo = valor * (1 - porcentagem) # o 1 equivale a 100% - a tolerancia em decimal
        maximo = valor * (1 + porcentagem) # o 1 equivale a 100% + a tolerancia em decimal
        resultado.config(text=f"Valor: {escalas(valor)} ±{tol_val}%\n"
                              f"Mínimo: {escalas(minimo)} | Máximo: {escalas(maximo)}")# valor mínimo de acordo com a variação da tolerância
                                                                                       # valor máximo de acordo com a variação da tolerância
        resistor(encontrado[0], encontrado[1], encontrado[2], tolerancia_sel) # desenha o resistor de acordo com a cores escolhidas

    except ValueError:
        resultado.config(text="Digite um valor numérico válido!") # verifica se o valor é válido
        
        
botao = tk.Button(janela, text="Calcular resistência", command=calcular) # botão de cor para resistência
botao.grid(row=4, column=0, columnspan=2, pady=10)

btn_converter = tk.Button(frame_valor, text="Converter", command=valor_para_cores) # botão de resistência para cor
btn_converter.grid(row=1, column=0, columnspan=3, pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 10, "bold")) # onde msotra o resultado maximo e minimo
resultado.grid(row=5, column=0, columnspan=3, pady=5)


canvas = tk.Canvas(janela, width=600, height=200, bg="#FFFFFF") # cria a área de desenho
canvas.grid(row=6, column=0, columnspan=3, pady=10)

resistor()

janela.mainloop()