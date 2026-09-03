import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title(text="Tentativa")
class CalculadoraResistor:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Resistor")
        self.root.geometry("600 x 800")
        self.root.configure(bg="#e8edf3")
        self.root.resizable(False, False)

        # Mapeamento de cores para valores
        self.cores_digito = {
            "preto": (0, "#000000"),
            "marrom": (1, "#8B4513"),
            "vermelho": (2, "#FF0000"),
            "laranja": (3, "#FFA500"),
            "amarelo": (4, "#FFFF00"),
            "verde": (5, "#008000"),
            "azul": (6, "#0000FF"),
            "violeta": (7, "#8A2BE2"),
            "cinza": (8, "#808080"),
            "branco": (9, "#FFFFFF")
        }

        self.cores_mult = {
            "preto": (1, "#000000"),
            "marrom": (10, "#8B4513"),
            "vermelho": (100, "#FF0000"),
            "laranja": (1000, "#FFA500"),
            "amarelo": (10000, "#FFFF00"),
            "verde": (100000, "#008000"),
            "azul": (1000000, "#0000FF"),
            "dourado": (0.1, "#FFD700"),
            "prateado": (0.01, "#C0C0C0")
        }

        self.setup_ui()

    def setup_ui(self):
        # Card Principal
        card = tk.Frame(self.root, bg="#ffffff", bd=1, relief="solid")
        card.pack(fill="both", expand=True, padx=15, pady=15)

        # Título interno
        lbl_titulo = tk.Label(card, text="Calculadora de Resistor", font=("Arial", 16, "bold"), bg="#ffffff", fg="#1d2b44")
        lbl_titulo.pack(anchor="w", padx=20, pady=(20, 15))

        # Opção de entrada (Radiobuttons)
        lbl_radio = tk.Label(card, text="Como deseja informar o resistor?", font=("Arial", 9, "bold"), bg="#ffffff")
        lbl_radio.pack(anchor="w", padx=20, pady=(0, 5))

        self.var_tipo = tk.StringVar(value="cores")
        frame_radio = tk.Frame(card, bg="#ffffff")
        frame_radio.pack(anchor="w", padx=20, pady=(0, 15))

        rb_valor = tk.Radiobutton(frame_radio, text="Valor da resistência", variable=self.var_tipo, value="valor", bg="#ffffff")
        rb_cores = tk.Radiobutton(frame_radio, text="Cores do resistor", variable=self.var_tipo, value="cores", bg="#ffffff")
        rb_valor.pack(side="left", padx=(0, 10))
        rb_cores.pack(side="left")

        # Seleção de Cores (Dropdowns)
        frame_selects = tk.Frame(card, bg="#ffffff")
        frame_selects.pack(fill="x", padx=20, pady=(0, 15))

        # Banda 1
        f_b1 = tk.Frame(frame_selects, bg="#ffffff")
        f_b1.pack(side="left", expand=True, fill="x", padx=(0, 5))
        tk.Label(f_b1, text="Banda 1:", font=("Arial", 8), bg="#ffffff").pack(anchor="w")
        self.cb_b1 = ttk.Combobox(f_b1, values=list(self.cores_digito.keys()), state="readonly", width=10)
        self.cb_b1.set("vermelho")
        self.cb_b1.pack(fill="x")

        # Banda 2
        f_b2 = tk.Frame(frame_selects, bg="#ffffff")
        f_b2.pack(side="left", expand=True, fill="x", padx=5)
        tk.Label(f_b2, text="Banda 2:", font=("Arial", 8), bg="#ffffff").pack(anchor="w")
        self.cb_b2 = ttk.Combobox(f_b2, values=list(self.cores_digito.keys()), state="readonly", width=10)
        self.cb_b2.set("vermelho")
        self.cb_b2.pack(fill="x")

        # Multiplicador
        f_mult = tk.Frame(frame_selects, bg="#ffffff")
        f_mult.pack(side="left", expand=True, fill="x", padx=(5, 0))
        tk.Label(f_mult, text="Multiplicador:", font=("Arial", 8), bg="#ffffff").pack(anchor="w")
        self.cb_mult = ttk.Combobox(f_mult, values=list(self.cores_mult.keys()), state="readonly", width=10)
        self.cb_mult.set("laranja")
        self.cb_mult.pack(fill="x")

        # Botão Calcular
        btn_calcular = tk.Button(
            card, text="Calcular resistência", bg="#108e66", fg="white",
            font=("Arial", 9, "bold"), bd=0, padx=12, pady=6, cursor="hand2",
            command=self.calcular
        )
        btn_calcular.pack(anchor="w", padx=20, pady=(0, 15))

        # Resultado
        self.lbl_resultado = tk.Label(card, text="Resistência: 22.00 kΩ ±0.1%", font=("Arial", 11, "bold"), bg="#ffffff", fg="#000000")
        self.lbl_resultado.pack(anchor="w", padx=20, pady=(0, 15))

        # Box de Exibição do Resistor
        frame_resistor_box = tk.Frame(card, bg="#f9f9f9", bd=1, relief="solid")
        frame_resistor_box.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        tk.Label(frame_resistor_box, text="Resistor de 4 faixas", font=("Arial", 11, "bold"), bg="#f9f9f9").pack(pady=(10, 15))

        # Desenho do Resistor (Canvas)
        self.canvas = tk.Canvas(frame_resistor_box, width=320, height=60, bg="#f9f9f9", highlightthickness=0)
        self.canvas.pack()

        # Rótulos de Texto das Cores
        self.frame_labels = tk.Frame(frame_resistor_box, bg="#f9f9f9")
        self.frame_labels.pack(fill="x", pady=(5, 10))

        self.lbl_cor1 = tk.Label(self.frame_labels, text="Vermelho", font=("Arial", 8), bg="#f9f9f9", width=8)
        self.lbl_cor1.pack(side="left", expand=True)

        self.lbl_cor2 = tk.Label(self.frame_labels, text="Vermelho", font=("Arial", 8), bg="#f9f9f9", width=8)
        self.lbl_cor2.pack(side="left", expand=True)

        self.lbl_cor3 = tk.Label(self.frame_labels, text="Laranja", font=("Arial", 8), bg="#f9f9f9", width=8)
        self.lbl_cor3.pack(side="left", expand=True)

        self.lbl_cor4 = tk.Label(self.frame_labels, text="Violeta", font=("Arial", 8), bg="#f9f9f9", width=8)
        self.lbl_cor4.pack(side="left", expand=True)

        # Desenha a ilustração inicial
        self.desenhar_resistor("#FF0000", "#FF0000", "#FFA500", "#8A2BE2")

    def desenhar_resistor(self, c1, c2, c3, c4):
        self.canvas.delete("all")
        # Pinos metálicos
        self.canvas.create_line(10, 30, 60, 30, fill="#888888", width=3)
        self.canvas.create_line(260, 30, 310, 30, fill="#888888", width=3)

        # Corpo do resistor
        self.canvas.create_rectangle(60, 10, 260, 50, fill="#E2CCA1", outline="#B3A078", width=2)

        # Faixas de cores
        self.canvas.create_rectangle(90, 10, 102, 50, fill=c1, width=0)
        self.canvas.create_rectangle(130, 10, 142, 50, fill=c2, width=0)
        self.canvas.create_rectangle(170, 10, 182, 50, fill=c3, width=0)
        self.canvas.create_rectangle(210, 10, 222, 50, fill=c4, width=0)

    def calcular(self):
        c1 = self.cb_b1.get()
        c2 = self.cb_b2.get()
        c3 = self.cb_mult.get()

        val1, hex1 = self.cores_digito[c1]
        val2, hex2 = self.cores_digito[c2]
        mult, hex3 = self.cores_mult[c3]
        hex4 = "#8A2BE2"  # Violeta fixo da tolerancia da imagem

        # Cálculo da resistência
        resistencia = ((val1 * 10) + val2) * mult

        # Formatação do texto (Ω, kΩ, MΩ)
        if resistencia >= 1_000_000:
            texto_res = f"{resistencia / 1_000_000:.2f} MΩ"
        elif resistencia >= 1_000:
            texto_res = f"{resistencia / 1_000:.2f} kΩ"
        else:
            texto_res = f"{resistencia:.2f} Ω"

        self.lbl_resultado.config(text=f"Resistência: {texto_res} ±0.1%")

        # Atualizar os rótulos de texto
        self.lbl_cor1.config(text=c1.capitalize())
        self.lbl_cor2.config(text=c2.capitalize())
        self.lbl_cor3.config(text=c3.capitalize())

        # Redesenhar faixas no resistor
        self.desenhar_resistor(hex1, hex2, hex3, hex4)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraResistor(root)
    root.mainloop()