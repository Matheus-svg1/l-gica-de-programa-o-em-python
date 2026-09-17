import tkinter as tk
from tkinter import ttk, Canvas

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.geometry("800x650")

CORES = [
    "preto", "marrom", "vermelho", "laranja", "amarelo",
    "verde", "azul", "violeta", "cinza", "branco"
]

cores_tolerancia = [
    "marrom", "vermelho", "verde", "azul", "violeta",
    "cinza", "dourado", "prata"
]

# Dicionários auxiliares de dados
MAPA_VALORES = {cor: idx for idx, cor in enumerate(CORES)}

MAPA_MULTIPLICADORES = {
    "preto": 1, "marrom": 10, "vermelho": 100, "laranja": 1_000,
    "amarelo": 10_000, "verde": 100_000, "azul": 1_000_000,
    "violeta": 10_000_000, "cinza": 100_000_000, "branco": 1_000_000_000
}

MAPA_TOLERANCIA = {
    "marrom": 1, "vermelho": 2, "verde": 0.5, "azul": 0.25,
    "violeta": 0.1, "cinza": 0.05, "dourado": 5, "prata": 10
}

# --- INTERFACE: Seção Cores -> Valor ---
tk.Label(janela, text="Banda 1").grid(row=0, column=0, sticky="e", padx=5, pady=2)
combo1 = ttk.Combobox(janela, values=CORES, state="readonly")
combo1.grid(row=0, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Banda 2").grid(row=1, column=0, sticky="e", padx=5, pady=2)
combo2 = ttk.Combobox(janela, values=CORES, state="readonly")
combo2.grid(row=1, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Banda 3").grid(row=2, column=0, sticky="e", padx=5, pady=2)
combo3 = ttk.Combobox(janela, values=CORES, state="readonly")
combo3.grid(row=2, column=1, sticky="w", padx=5, pady=2)

tk.Label(janela, text="Tolerância").grid(row=3, column=0, sticky="e", padx=5, pady=2)
combo4 = ttk.Combobox(janela, values=cores_tolerancia, state="readonly")
combo4.grid(row=3, column=1, sticky="w", padx=5, pady=2)

# --- INTERFACE: Seção Valor -> Cores ---
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


# --- FUNÇÕES DE APOIO COM HEXADECIMAL ---
def faixa_resistor_hex(cor):
    # Mapeamento completo de cores em formato Hexadecimal (#HEX)
    hex_map = {
        "preto": "#000000",
        "marrom": "#8B4513",
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
    return hex_map.get(cor, "#F5F5DC")  # Retorna cor bege padrão caso não encontre


def escalas(ohms):
    if ohms >= 1_000_000:
        return f"{ohms / 1_000_000:g} MΩ"
    if ohms >= 1_000:
        return f"{ohms / 1_000:g} kΩ"
    return f"{ohms:g} Ω"


def resistor(cor1="", cor2="", cor3="", cor4=""):
    canvas.delete("all")

    # Fios em Hexadecimal (#555555)
    canvas.create_line(50, 100, 150, 100, width=5, fill="black")
    canvas.create_line(450, 100, 550, 100, width=5, fill="black")

    # Corpo em Hexadecimal (#F5F5DC - Beige / #000000 - Borda)
    canvas.create_rectangle(150, 70, 450, 130, fill="#F5F5DC", outline="black")

    # Faixas coloridas aplicadas em Hexadecimal
    if cor1: canvas.create_rectangle(180, 70, 200, 130, fill=faixa_resistor_hex(cor1), outline="black")
    if cor2: canvas.create_rectangle(230, 70, 250, 130, fill=faixa_resistor_hex(cor2), outline="black")
    if cor3: canvas.create_rectangle(280, 70, 300, 130, fill=faixa_resistor_hex(cor3), outline="black")
    if cor4: canvas.create_rectangle(375, 70, 400, 130, fill=faixa_resistor_hex(cor4), outline="black")

    # Textos
    canvas.create_text(190, 150, text=cor1, font=("Arial", 8))
    canvas.create_text(240, 150, text=cor2, font=("Arial", 8))
    canvas.create_text(290, 150, text=cor3, font=("Arial", 8))
    canvas.create_text(385, 150, text=cor4, font=("Arial", 8))


# --- LÓGICA DE CÁLCULO ---
def calcular():
    cor1, cor2, cor3, cor4 = combo1.get(), combo2.get(), combo3.get(), combo4.get()

    if not (cor1 and cor2 and cor3 and cor4):
        resultado.config(text="Selecione todas as cores para calcular!")
        return

    numero = MAPA_VALORES[cor1] * 10 + MAPA_VALORES[cor2]
    resistencia = numero * MAPA_MULTIPLICADORES[cor3]
    tol = MAPA_TOLERANCIA[cor4]

    minimo = resistencia - (resistencia * tol / 100)
    maximo = resistencia + (resistencia * tol / 100)

    resultado.config(
        text=f"Resistência: {escalas(resistencia)}  ±{tol}%\n"
             f"Mínimo: {escalas(minimo)} | Máximo: {escalas(maximo)}"
    )
    resistor(cor1, cor2, cor3, cor4)


def valor_para_cores():
    try:
        valor = float(entrada_resistencia.get())
        unidade = unidade_var.get()
        fator_unidade = {"Ω": 1, "KΩ": 1_000, "MΩ": 1_000_000}[unidade]
        valor *= fator_unidade

        if valor <= 0:
            resultado.config(text="Digite um valor maior que zero!")
            return

        encontrado = None

        for cor_mult, fator in MAPA_MULTIPLICADORES.items():
            if fator > 0 and 10 <= (valor / fator) <= 99:
                numero = valor / fator
                if numero.is_integer():
                    numero = int(numero)
                    d1, d2 = numero // 10, numero % 10
                    cor1 = CORES[d1]
                    cor2 = CORES[d2]
                    encontrado = (cor1, cor2, cor_mult)
                    break

        if not encontrado:
            resultado.config(text="Valor de resistência não padrão/representável!")
            return

        tolerancia_sel = combo4.get() or "dourado"

        combo1.set(encontrado[0])
        combo2.set(encontrado[1])
        combo3.set(encontrado[2])
        combo4.set(tolerancia_sel)

        tol_val = MAPA_TOLERANCIA[tolerancia_sel]
        resultado.config(text=f"Valor: {escalas(valor)} ±{tol_val}%")

        resistor(encontrado[0], encontrado[1], encontrado[2], tolerancia_sel)

    except ValueError:
        resultado.config(text="Digite um valor numérico válido!")


# --- COMPONENTES FINAIS ---
botao = tk.Button(janela, text="Calcular resistência", command=calcular)
botao.grid(row=4, column=0, columnspan=2, pady=10)

btn_converter = tk.Button(frame_valor, text="Converter", command=valor_para_cores)
btn_converter.grid(row=1, column=0, columnspan=3, pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 10, "bold"))
resultado.grid(row=5, column=0, columnspan=3, pady=5)

# Fundo do Canvas em Hexadecimal (#FFFFFF)
canvas = tk.Canvas(janela, width=600, height=200, bg="#FFFFFF")
canvas.grid(row=6, column=0, columnspan=3, pady=10)

resistor()

janela.mainloop()