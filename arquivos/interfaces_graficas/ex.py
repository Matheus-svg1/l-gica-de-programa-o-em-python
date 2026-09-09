import tkinter as tk
from tkinter import ttk


# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()
janela.title("Calculadora de Resistor")
janela.geometry("720x650")
janela.resizable(False, False)


# ==========================================
# CORES E VALORES
# ==========================================

cores = [
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

valores = {
    "preto": 0,
    "marrom": 1,
    "vermelho": 2,
    "laranja": 3,
    "amarelo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "cinza": 8,
    "branco": 9
}

multiplicadores = {
    "preto": 1,
    "marrom": 10,
    "vermelho": 100,
    "laranja": 1000,
    "amarelo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "cinza": 100000000,
    "branco": 1000000000
}

tolerancias = {
    "marrom": "±1%",
    "vermelho": "±2%",
    "dourado": "±5%",
    "prateado": "±10%"
}


# ==========================================
# FUNÇÕES
# ==========================================

def formatar_resistencia(valor):

    if valor >= 1000000000:
        return f"{valor / 1000000000:.2f} GΩ"

    elif valor >= 1000000:
        return f"{valor / 1000000:.2f} MΩ"

    elif valor >= 1000:
        return f"{valor / 1000:.2f} kΩ"

    else:
        return f"{valor:.2f} Ω"


def cor_tkinter(cor):

    mapa = {
        "preto": "black",
        "marrom": "brown",
        "vermelho": "red",
        "laranja": "orange",
        "amarelo": "yellow",
        "verde": "green",
        "azul": "blue",
        "violeta": "purple",
        "cinza": "gray",
        "branco": "white",
        "dourado": "gold",
        "prateado": "silver"
    }

    return mapa.get(cor, "white")


# ==========================================
# DESENHAR RESISTOR
# ==========================================

def desenhar_resistor(cor1, cor2, cor3, cor4):

    canvas.delete("all")

    # título
    canvas.create_text(
        320,
        30,
        text="Resistor de 4 faixas",
        font=("Arial", 18, "bold")
    )

    # fio esquerdo
    canvas.create_line(
        20, 100,
        90, 100,
        width=7,
        fill="gray"
    )

    # fio direito
    canvas.create_line(
        550, 100,
        620, 100,
        width=7,
        fill="gray"
    )

    # corpo do resistor
    canvas.create_rectangle(
        90, 65,
        550, 135,
        fill="#f5e4a8",
        outline="#555555",
        width=2
    )

    # faixas
    largura = 20

    posicoes = [150, 220, 290, 360]

    for posicao, cor in zip(posicoes, [cor1, cor2, cor3, cor4]):

        canvas.create_rectangle(
            posicao,
            65,
            posicao + largura,
            135,
            fill=cor_tkinter(cor),
            outline="black"
        )

    # nomes das cores
    nomes = [cor1, cor2, cor3, cor4]

    for posicao, nome in zip(posicoes, nomes):

        canvas.create_text(
            posicao + 10,
            165,
            text=nome.capitalize(),
            font=("Arial", 10)
        )


# ==========================================
# CALCULAR PELAS CORES
# ==========================================

def calcular_cores():

    cor1 = combo_banda1.get()
    cor2 = combo_banda2.get()
    cor3 = combo_multiplicador.get()
    cor4 = combo_tolerancia.get()

    if cor1 == "" or cor2 == "" or cor3 == "" or cor4 == "":
        resultado.config(
            text="Selecione todas as cores."
        )
        return

    numero = valores[cor1] * 10 + valores[cor2]

    multiplicador = multiplicadores[cor3]

    resistencia = numero * multiplicador

    tolerancia = tolerancias[cor4]

    resultado.config(
        text=f"Resistência: {formatar_resistencia(resistencia)} {tolerancia}"
    )

    desenhar_resistor(
        cor1,
        cor2,
        cor3,
        cor4
    )


# ==========================================
# CALCULAR CORES A PARTIR DO VALOR
# ==========================================

def calcular_valor():

    texto = entrada_valor.get()

    if texto == "":
        resultado.config(
            text="Digite o valor da resistência."
        )
        return

    try:
        valor = float(texto)

    except ValueError:
        resultado.config(
            text="Digite um valor numérico válido."
        )
        return

    tolerancia = combo_tolerancia_valor.get()

    if tolerancia == "":
        resultado.config(
            text="Selecione a tolerância."
        )
        return

    # Encontrar duas primeiras faixas
    if valor < 10:
        resultado.config(
            text="Digite um valor maior ou igual a 10 Ω."
        )
        return

    # Descobrir potência de 10
    numero = valor
    potencia = 0

    while numero >= 100:
        numero /= 10
        potencia += 1

    primeiro = int(numero // 10)
    segundo = int(numero % 10)

    # Ajuste para valores decimais
    if primeiro == 0:
        resultado.config(
            text="Valor não suportado."
        )
        return

    cor1 = cores[primeiro]
    cor2 = cores[segundo]

    cor3 = cores[potencia]

    cor4 = tolerancia

    resultado.config(
        text=f"Resistência: {formatar_resistencia(valor)} "
             f"{tolerancias[tolerancia]}"
    )

    desenhar_resistor(
        cor1,
        cor2,
        cor3,
        cor4
    )


# ==========================================
# MUDAR PARA MODO CORES
# ==========================================

def mostrar_cores():

    # esconder modo valor
    frame_valor.grid_remove()

    # mostrar modo cores
    frame_cores.grid()

    botao_calcular.config(
        text="Calcular resistência",
        command=calcular_cores
    )

    resultado.config(
        text="Digite o valor da resistência ou selecione as cores."
    )

    canvas.delete("all")
    canvas.create_text(
        320,
        100,
        text="Aguarde a seleção do modo",
        font=("Arial", 16)
    )


# ==========================================
# MUDAR PARA MODO VALOR
# ==========================================

def mostrar_valor():

    # esconder modo cores
    frame_cores.grid_remove()

    # mostrar modo valor
    frame_valor.grid()

    botao_calcular.config(
        text="Calcular cores",
        command=calcular_valor
    )

    resultado.config(
        text="Digite o valor da resistência ou selecione as cores."
    )

    canvas.delete("all")
    canvas.create_text(
        320,
        100,
        text="Aguarde a seleção do modo",
        font=("Arial", 16)
    )


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    janela,
    text="Calculadora de Resistor",
    font=("Arial", 22, "bold")
)

titulo.pack(
    anchor="w",
    padx=30,
    pady=(20, 10)
)


# ==========================================
# FRAME PRINCIPAL
# ==========================================

principal = tk.Frame(
    janela,
    bg="white"
)

principal.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)


# ==========================================
# PERGUNTA DO MODO
# ==========================================

label_modo = tk.Label(
    principal,
    text="Como deseja informar o resistor?",
    font=("Arial", 12, "bold"),
    bg="white"
)

label_modo.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="w",
    pady=(10, 5)
)


modo = tk.StringVar(value="cores")


radio_valor = tk.Radiobutton(
    principal,
    text="Valor da resistência",
    variable=modo,
    value="valor",
    command=mostrar_valor,
    bg="white"
)

radio_valor.grid(
    row=1,
    column=0,
    sticky="w"
)


radio_cores = tk.Radiobutton(
    principal,
    text="Cores do resistor",
    variable=modo,
    value="cores",
    command=mostrar_cores,
    bg="white"
)

radio_cores.grid(
    row=1,
    column=1,
    sticky="w"
)


# ==========================================
# FRAME DAS CORES
# ==========================================

frame_cores = tk.Frame(
    principal,
    bg="white"
)

frame_cores.grid(
    row=2,
    column=0,
    columnspan=4,
    sticky="w",
    pady=15
)


# Banda 1
tk.Label(
    frame_cores,
    text="Banda 1:",
    bg="white"
).grid(row=0, column=0, sticky="w")

combo_banda1 = ttk.Combobox(
    frame_cores,
    values=cores,
    state="readonly",
    width=14
)

combo_banda1.grid(
    row=1,
    column=0,
    padx=(0, 15)
)


# Banda 2
tk.Label(
    frame_cores,
    text="Banda 2:",
    bg="white"
).grid(row=0, column=1, sticky="w")

combo_banda2 = ttk.Combobox(
    frame_cores,
    values=cores,
    state="readonly",
    width=14
)

combo_banda2.grid(
    row=1,
    column=1,
    padx=(0, 15)
)


# Multiplicador
tk.Label(
    frame_cores,
    text="Multiplicador:",
    bg="white"
).grid(row=0, column=2, sticky="w")

combo_multiplicador = ttk.Combobox(
    frame_cores,
    values=cores,
    state="readonly",
    width=14
)

combo_multiplicador.grid(
    row=1,
    column=2,
    padx=(0, 15)
)


# Tolerância
tk.Label(
    frame_cores,
    text="Tolerância:",
    bg="white"
).grid(row=0, column=3, sticky="w")

combo_tolerancia = ttk.Combobox(
    frame_cores,
    values=["marrom", "vermelho", "dourado", "prateado"],
    state="readonly",
    width=14
)

combo_tolerancia.grid(
    row=1,
    column=3
)


# ==========================================
# FRAME DO VALOR
# ==========================================

frame_valor = tk.Frame(
    principal,
    bg="white"
)

frame_valor.grid(
    row=2,
    column=0,
    columnspan=4,
    sticky="w",
    pady=15
)

tk.Label(
    frame_valor,
    text="Valor da resistência (Ω):",
    bg="white"
).grid(
    row=0,
    column=0,
    sticky="w"
)

entrada_valor = tk.Entry(
    frame_valor,
    width=20,
    font=("Arial", 12)
)

entrada_valor.grid(
    row=1,
    column=0,
    padx=(0, 30)
)


tk.Label(
    frame_valor,
    text="Tolerância:",
    bg="white"
).grid(
    row=0,
    column=1,
    sticky="w"
)

combo_tolerancia_valor = ttk.Combobox(
    frame_valor,
    values=["marrom", "vermelho", "dourado", "prateado"],
    state="readonly",
    width=15
)

combo_tolerancia_valor.grid(
    row=1,
    column=1
)


# ==========================================
# BOTÃO
# ==========================================

botao_calcular = tk.Button(
    principal,
    text="Calcular resistência",
    command=calcular_cores,
    font=("Arial", 11, "bold"),
    bg="#25a89d",
    fg="white",
    padx=10,
    pady=8
)

botao_calcular.grid(
    row=3,
    column=0,
    sticky="w",
    pady=10
)


# ==========================================
# RESULTADO
# ==========================================

resultado = tk.Label(
    principal,
    text="Digite o valor da resistência ou selecione as cores.",
    font=("Arial", 12, "bold"),
    bg="white"
)

resultado.grid(
    row=4,
    column=0,
    columnspan=4,
    sticky="w",
    pady=10
)


# ==========================================
# CANVAS DO RESISTOR
# ==========================================

canvas = tk.Canvas(
    principal,
    width=640,
    height=230,
    bg="#f8f9fa",
    highlightthickness=1,
    highlightbackground="#d5dce3"
)

canvas.grid(
    row=5,
    column=0,
    columnspan=4,
    pady=10
)

canvas.create_text(
    320,
    100,
    text="Aguarde a seleção do modo",
    font=("Arial", 16)
)


# ==========================================
# INICIAR
# ==========================================

frame_valor.grid_remove()

janela.mainloop()