import tkinter as tk
import os
from tkinter import messagebox

janela = tk.Tk()
janela.title("Caixa eletrônico")
janela.geometry("600x750")

tk.Label(janela, text = "Bem-vindo ao Caixa Eletrônico!!")
saldo_inicial = 1000

arquivo =" contas.txt"

cedulas = [100, 50, 20, 10, 5, 2]

saldo = 0
conta_atual =""

def buscar_saldo(conta_digitada):
    """Procura a conta no arquivo. Retorna o saldo salvo ou 1000 se for nova."""
    if not os.path.exists(arquivo):
        return 1000

    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 2 and dados[0] == conta_digitada:
                return int(dados[1])
                
    return 1000

def salvar_dados(conta_digitada, saldo_atual):
    "Atualiza ou cria o arquivo onde vai ser guardando as informações de login"
    linhas = []
    conta_encontrada = False
    
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 2:
                    linhas.append(f"{conta_digitada};{saldo_atual}\n")
                    conta_encontrada = True
                else:
                    linhas.apppen(linha)
                    
    if not conta_encontrada:
        linhas.append(f"{conta_digitada};{saldo_atual}\n")
    with open(arquivo, "w") as arquivo:
        arquivo.writelines(linhas)
        
        
#TELA

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()
        
# TELA LOGIN

def tela_login():
    limpar_tela()
    

    tk.Label(janela, text="Caixa Eletrônico", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Label(janela, text="Digite a conta:").pack()
    entrada_conta = tk.Entry(janela)
    entrada_conta.pack(pady=5)


    tk.Label(janela, text="Digite a senha:").pack()
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack(pady=5)

    def entrar():
        global conta_atual, saldo
    
        conta = entrada_conta.get().strip()
        senha = entrada_senha.get().strip()
        
        if conta == "" or senha == "":
            messagebox.showerror("Erro, Preencha a conta e a senha!")
            return
        
        
        conta_atual = conta
        saldo = buscar_saldo(conta)
        
        messagebox.showinfo(
            "Bem-vindo",
                f"Sessão iniciada na conta {conta}.\nSaldo atual: R${saldo},00")
    
    
    
def menu ():
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print(" 4 - Sair")

    opcao = input("Escolha uma opção !")
    menu()

    if opcao == "0":
        pass



tela_login()
janela.mainloop()