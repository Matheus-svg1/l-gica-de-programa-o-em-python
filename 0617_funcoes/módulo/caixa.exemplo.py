import os
import tkinter as tk
from tkinter import messagebox

# ==========================================
# CONFIGURAÇÕES
# ==========================================
ARQUIVO = "dados.txt"
CEDULAS = [100, 50, 20, 10, 5, 2]

saldo = 1000
conta_atual = ""



#import tkinter as tk
#
#janela = tk.Tk()
#janela.title("Exemplo Checkbutton Senha")
#janela.geometry("300x200")
#
#tk.Label(janela, text="Digite sua senha:").pack(pady=5)
#
## Campo de entrada inicializado ocultando a senha com "*"
#entrada_senha = tk.Entry(janela, show="*")
#entrada_senha.pack(pady=5)
#
## Variável do Tkinter para guardar o estado (True ou False) da caixa
#mostrar_senha_var = tk.BooleanVar()
#
#
#def alternar_senha():
#    # Se a caixa estiver marcada (True), mostra o texto em limpo
#    if mostrar_senha_var.get():
#        entrada_senha.config(show="")
#    # Se estiver desmarcada (False), oculta com "*"
#    else:
#        entrada_senha.config(show="*")
#
#
## Criação do Checkbutton
#check_senha = tk.Checkbutton(
#    janela,
#    text="Mostrar senha",
#    variable=mostrar_senha_var,
#    command=alternar_senha
#)
#check_senha.pack(pady=5)
#
#janela.mainloop()







# ==========================================
# FUNÇÕES DE PERSISTÊNCIA (ARQUIVO)
# ==========================================
def buscar_saldo(conta_digitada):
    """Procura a conta no arquivo. Retorna o saldo salvo ou 1000 se for nova."""
    if not os.path.exists(ARQUIVO):
        return 1000

    with open(ARQUIVO, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 2 and dados[0] == conta_digitada:
                return int(dados[1])
                
    return 1000


def salvar_saldo(conta_digitada, saldo_atual):
    """Atualiza ou cria o registro da conta no arquivo de texto."""
    linhas = []
    conta_encontrada = False

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 2:
                    if dados[0] == conta_digitada:
                        linhas.append(f"{conta_digitada};{saldo_atual}\n")
                        conta_encontrada = True
                    else:
                        linhas.append(linha)

    if not conta_encontrada:
        linhas.append(f"{conta_digitada};{saldo_atual}\n")

    with open(ARQUIVO, "w") as arquivo:
        arquivo.writelines(linhas)


# ==========================================
# TELA E NAVEGAÇÃO
# ==========================================
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()


def tela_login():
    limpar_tela()

    tk.Label(
        janela, 
        text="Caixa Eletrônico", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(janela, text="Digite a conta:").pack()
    entrada_conta = tk.Entry(janela)
    entrada_conta.pack(pady=5)
    entrada_conta.focus()

    tk.Label(janela, text="Digite a senha:").pack()
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack(pady=5)

    def entrar():
        global conta_atual, saldo

        conta = entrada_conta.get().strip()
        senha = entrada_senha.get().strip()

        if conta == "" or senha == "":
            messagebox.showerror("Erro", "Preencha a conta e a senha!")
            return

        conta_atual = conta
        saldo = buscar_saldo(conta)

        messagebox.showinfo(
            "Bem-vindo", 
            f"Sessão iniciada na conta '{conta}'.\nSaldo atual: R$ {saldo},00"
        )
        mostrar_menu()

    tk.Button(
        janela, 
        text="Entrar", 
        width=15, 
        height=2, 
        command=entrar
    ).pack(pady=20)


def mostrar_menu():
    limpar_tela()

    tk.Label(
        janela, 
        text="MENU PRINCIPAL", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        janela, 
        text=f"Conta Ativa: {conta_atual}", 
        font=("Arial", 10, "italic")
    ).pack(pady=5)

    tk.Button(
        janela, 
        text="1 - Consultar saldo", 
        width=25, 
        height=2, 
        command=consultar_saldo
    ).pack(pady=8)

    tk.Button(
        janela, 
        text="2 - Sacar", 
        width=25, 
        height=2, 
        command=tela_saque
    ).pack(pady=8)

    tk.Button(
        janela, 
        text="3 - Depositar", 
        width=25, 
        height=2, 
        command=tela_deposito
    ).pack(pady=8)

    tk.Button(
        janela, 
        text="4 - Sair", 
        width=25, 
        height=2, 
        command=sair
    ).pack(pady=8)


# ==========================================
# OPERAÇÕES DO CAIXA
# ==========================================
def consultar_saldo():
    messagebox.showinfo("Saldo", f"Seu saldo atual é:\n\nR$ {saldo},00")


def tela_deposito():
    limpar_tela()

    tk.Label(
        janela, 
        text="DEPÓSITO", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(janela, text="Digite o valor para depósito:").pack()
    entrada_valor = tk.Entry(janela)
    entrada_valor.pack(pady=10)
    entrada_valor.focus()

    def realizar_deposito():
        global saldo
        valor_texto = entrada_valor.get().strip()

        # Validação simples de número inteiro positivo
        try:
            valor = int(valor_texto)
            
        except:
            messagebox.showerror("Erro", "Digite apenas valores inteiros e positivos!")
            return

        if valor <=0:
            messagebox.showerror("Erro", "O valor deve ser maior que zero!")
            return

        saldo += valor
        messagebox.showinfo("Sucesso", f"Depósito efetuado!\nNovo saldo: R$ {saldo},00")
        mostrar_menu()

    tk.Button(janela, text="Depositar", width=15, command=realizar_deposito).pack(pady=10)
    tk.Button(janela, text="Voltar", width=15, command=mostrar_menu).pack(pady=5)


def tela_saque():
    limpar_tela()

    tk.Label(
        janela, 
        text="SAQUE", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(janela, text="Digite o valor para saque:").pack()
    entrada_valor = tk.Entry(janela)
    entrada_valor.pack(pady=10)
    entrada_valor.focus()

    def realizar_saque():
        global saldo
        valor_texto = entrada_valor.get().strip()

        if not valor_texto.isdigit():
            messagebox.showerror("Erro", "Digite apenas valores inteiros e positivos!")
            return

        valor = int(valor_texto)

        if valor <= 0:
            messagebox.showerror("Erro", "O valor deve ser maior que zero!")
            return

        if valor > saldo:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return

        # ==================================
        # CÁLCULO DAS CÉDULAS (INICIANTE)
        # ==================================
        restante = valor
        quantidade_notas = {}

        for cedula in CEDULAS:
            quantidade_notas[cedula] = restante // cedula
            restante = restante % cedula

        # Ajuste direto para casos específicos com notas de 5 e 2 (ex: R$ 6 ou R$ 8)
        if restante != 0 and quantidade_notas[5] > 0:
            quantidade_notas[5] -= 1
            restante += 5
            quantidade_notas[2] += restante // 2
            restante = restante % 2

        # Validação de valor incompatível com as notas disponíveis (ex: R$ 1, R$ 3)
        if restante != 0:
            messagebox.showerror(
                "Erro",
                "O caixa não consegue entregar esse valor exato!\n\n"
                "Cédulas disponíveis:\nR$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2."
            )
            return

        saldo -= valor

        # Montagem do recibo visual
        mensagem = "Saque realizado com sucesso!\n\nEntregar:\n"
        for cedula in CEDULAS:
            qtd = quantidade_notas[cedula]
            if qtd > 0:
                mensagem += f"- {qtd} cédula(s) de R$ {cedula}\n"

        mensagem += f"\nSaldo restante: R$ {saldo},00"
        messagebox.showinfo("Saque", mensagem)
        mostrar_menu()

    tk.Button(janela, text="Sacar", width=15, command=realizar_saque).pack(pady=10)
    tk.Button(janela, text="Voltar", width=15, command=mostrar_menu).pack(pady=5)


def sair():
    salvar_saldo(conta_atual, saldo)
    messagebox.showinfo(
        "Sair", 
        f"Saldo da conta '{conta_atual}' salvo com sucesso em '{ARQUIVO}'!"
    )
    tela_login()


# ==========================================
# JANELA PRINCIPAL
# ==========================================
janela = tk.Tk()
janela.title("Simulador de Caixa Eletrônico")
janela.geometry("450x550")
janela.resizable(False, False)

tela_login()
janela.mainloop()