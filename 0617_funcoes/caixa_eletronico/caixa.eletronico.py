import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Caixa eletrônico")
janela.geometry("600x750")

tk.Label(janela, text = "Bem-vindo ao Caixa Eletrônico!!")
saldo_inicial = 1000

 #Arquivo onde vai ser guardado as informações

cedulas = [100, 50, 20, 10, 5, 2] #valores das cedulas

saldo = 0 
conta_atual =""

ARQUIVO = "contas.txt"  #arquivo onde vai ser guardado as informações

def buscar_saldo(conta_digitada):# procura a conta no arquivo, retorna o saldo salvo ou 1000 se for nova
    try:
        with open(ARQUIVO, "r") as f: #abre o arquivo e pega todas as informações
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) == 2 and dados[0] == conta_digitada: #le se os dados forem iguais ele retorna a posição 1 do arquivo
                    return int(dados[1])
    except FileNotFoundError: # se der erro retorna que é conta nova
        return 1000
    return 1000


def salvar_dados(conta_digitada, saldo_atual):# atualiza o saldo da conta ou adiciona uma nova conta se não existir
    linhas = []
    conta_encontrada = False

    try:
        with open(ARQUIVO, "r") as f: #abre o arquivo e pega todas as informações
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) == 2:
                    if dados[0] == conta_digitada:
                        # atualiza o saldo da conta que esta sendo usada
                        linhas.append(f"{conta_digitada};{saldo_atual}\n")
                        conta_encontrada = True
                    else:
                        # mantém os dados das outras contas intactos
                        linhas.append(linha)
                else:
                    linhas.append(linha)
    except FileNotFoundError:
        # Se o arquivo ainda não existir, ele será criado
        pass

    # Se a conta não foi encontrada no arquivo, adiciona como uma nova entrada
    if not conta_encontrada:
        linhas.append(f"{conta_digitada};{saldo_atual}\n")

    # Reescreve o arquivo com a lista atualizada
    with open(ARQUIVO, "w") as f:
        f.writelines(linhas)
        
        
#TELA

def limpar_tela():
    for tela in janela.winfo_children(): # se tiver algo na janela do tkinter = vai ser apagado "O winfo_children guarda as informções que tem na janela"
        tela.destroy()
        
# TELA LOGIN

def tela_login(): #Criação da tela de login
    limpar_tela()
    

    tk.Label(janela, text="Caixa Eletrônico", font=("Arial", 20, "bold")).pack(pady=20) #Cria o texto de caixa eletrônico

    tk.Label(janela, text="Digite a conta:").pack() # Cria o texto de digite a conta e o campo de entrada
    entrada_conta = tk.Entry(janela)
    entrada_conta.pack(pady=5)


    tk.Label(janela, text="Digite a senha:").pack() #Cria o texto de digite a senha e campo de entrada
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack(pady=5)

    def entrar(): # Função do botão
        global conta_atual, saldo
    
        conta = entrada_conta.get().strip() #Pega as informações do campo de entrada da conta
        senha = entrada_senha.get().strip() #Pega as informações do campo de entr da da senha
        
        if conta == "" or senha == "": # se os campos estiverem vazios retorna esse erro
            messagebox.showerror("Erro", " Preencha a conta e a senha!")
            return
        
        
        conta_atual = conta
        saldo = buscar_saldo(conta)
        
        messagebox.showinfo( # mostra o nome da conta logada e o saldo
            "Bem-vindo",
                f"Sessão iniciada na conta {conta}.\nSaldo atual: R${saldo},00")
        menu()
    tk.Button( #botão de entrar
        janela,
        text = "Entrar",
        command= entrar
        ).pack()

    
def menu():
    limpar_tela()
    tk.Label(janela, text= "Bem-vindo ao menu!", font=("Arial", 15, "bold")).pack()

    tk.Button(janela, text= "1 - Consultar saldo", command= consultar_saldo, width=20, height=2).pack(pady=20)

    tk.Button(janela, text= "2 - Sacar", command= sacar, width=20, height=2).pack(pady=20)

    tk.Button(janela, text= "3 - Depositar", command= "", width=20, height=2).pack(pady=20)

    tk.Button(janela, text="4 - Sair", command= sair, width=20, height=2).pack(pady=20)
def consultar_saldo():
    messagebox.showinfo("Saldo", f"Seu saldo é {saldo},00")

def sacar():
    messagebox.showinfo("Saque", f"vazio por enquanto!!!")


def depositar():
    tk.Label(janela, text="SAQUE", font=("Arial", 20, "bold")).pack()
#def menu ():
    #print("1 - Consultar saldo")
    #print("2 - Sacar")
    #print("3 - Depositar")
    #print(" 4 - Sair")

    #opcao = input("Escolha uma opção !")
    #menu()

    #if opcao == "0":
     #   pass

def sair():
   salvar_dados(conta_atual, saldo) 
   messagebox.showinfo("Sair",f"Saldo da conta {conta_atual} foi salvo com sucesso em {ARQUIVO} !")
   tela_login()


tela_login()
janela.mainloop()