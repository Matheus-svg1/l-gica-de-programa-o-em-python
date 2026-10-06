import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Caixa eletrônico")
janela.geometry("450x550")

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
                        # mantém os dados das outras contas salvos
                        linhas.append(linha)
                else:
                    linhas.append(linha)
    except FileNotFoundError:
        # Se o arquivo ainda não existir, ele será criado
        pass

    # se a conta não foi encontrada no arquivo, adiciona como uma conta nova
    if not conta_encontrada:
        linhas.append(f"{conta_digitada};{saldo_atual}\n")

    # reescreve o arquivo com a lista atualizada
    with open(ARQUIVO, "w") as f:
        f.writelines(linhas)
        
        
#TELA

def limpar_tela():
    for tela in janela.winfo_children(): # se tiver algo na janela do tkinter = vai ser apagado "O winfo_children guarda as informções que tem na janela"
        tela.destroy()
        
# TELA LOGIN

def tela_login(): #criação da tela de login
    limpar_tela()
    

    tk.Label(janela, text="Caixa Eletrônico", font=("Arial", 20, "bold")).pack(pady=20) #cria o texto de caixa eletrônico

    tk.Label(janela, text="Digite a conta:").pack() # cria o texto de digite a conta e o campo de entrada
    entrada_conta = tk.Entry(janela)
    entrada_conta.pack(pady=5)


    tk.Label(janela, text="Digite a senha:").pack() #cria o texto de digite a senha e campo de entrada
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack(pady=5)

    def entrar(): # função do botão "Entrar"
        global conta_atual, saldo
    
        conta = entrada_conta.get().strip() #pega as informações do campo de entrada da conta
        senha = entrada_senha.get().strip() #pega as informações do campo de entr da da senha
        
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

    
def menu(): #criação do menu
    limpar_tela()
    tk.Label(janela, text= "Bem-vindo ao menu!", font=("Arial", 15, "bold")).pack() #texto de bem-vindo

    tk.Button(janela, text= "1 - Consultar saldo", command= consultar_saldo, width=20, height=2).pack(pady=20)#botão para consultar o saldo

    tk.Button(janela, text= "2 - Sacar", command= sacar, width=20, height=2).pack(pady=20)# botão para sacar

    tk.Button(janela, text= "3 - Depositar", command= depositar, width=20, height=2).pack(pady=20)#botao para depositar

    tk.Button(janela, text="4 - Sair", command= sair, width=20, height=2).pack(pady=20)#botao de sair
    
def consultar_saldo():                                     #função de cinsultar o saldo
    messagebox.showinfo("Saldo", f"Seu saldo é {saldo},00")

def sacar():
    limpar_tela()
    tk.Label(janela, text="SAQUE", font =("Arial", 20, "bold")).pack(pady=20)
    
    tk.Label(janela, text="Digite um valor para saque(R$):").pack()
    entrada_sq = tk.Entry(janela)
    entrada_sq.pack()
    
    def realizar_saque():
        global saldo
        valor_sq = entrada_sq.get().strip()
        
        
        try:
            valor = int(valor_sq)
        except:
            messagebox.showerror("Erro", "Digite apenas valores inteiros e positivos!")
            return
        
        if valor <=0:
            messagebox.showerror("Erro", "O valor deve ser maior que zaro!")
            return
        
        saldo -= valor
        
        messagebox.showinfo("Sucesso", f"Saque efetuado!\nNovo saldo: R${saldo},00")
        menu()
        
    tk.Button(janela, text="Sacar", width=15, command=realizar_saque).pack(pady=20)
    tk.Button(janela, text= "Voltar", width=15,command=menu).pack(pady=20)
        
    


def depositar(): #função para depositar
    limpar_tela()#limpa a tela
    tk.Label(janela, text="DEPÓSITO", font=("Arial", 20, "bold")).pack(pady=20)# cria uma nova aba para deposito
    
    tk.Label(janela, text= "Digite um valor para depósito(R$):").pack()# cria o texto
    entrada_dp =tk.Entry(janela,) #cria o campo de entrada para inserir o valor
    entrada_dp.pack()#adicona a conta á janela
    
    def realizar_deposito(): #realizar o deposito
        global saldo
        valor_dp = entrada_dp.get().strip() #cria uma variável que pega as informações do entry e tira os espaços
    
    
        try:
            valor = int(valor_dp) #valida se é inteiro
                
        except:
            messagebox.showerror("Erro", "Digite apenas valores inteiros e positivos!") #possível erro
            return
    
        if valor <=0: # se o valor for menor ou igual a zero...
            messagebox.showerror("Erro", "O valor deve ser maior que zero!")
            return
    
        saldo += valor# pega o saldo e soma com o valor de depósito
        messagebox.showinfo("Sucesso", f"Depósito efetuado!\nNovo saldo: R$ {saldo},00") #mensagem de depósito efetuado
        menu()
    
    tk.Button(janela, text="Depositar", width=15, command=realizar_deposito).pack(pady=10) #botão de depositar
    tk.Button(janela, text="Voltar", width=15, command=menu).pack(pady=5)
    
    
def sair():
   salvar_dados(conta_atual, saldo) 
   messagebox.showinfo("Sair",f"Sessão encerrada na conta {conta_atual} !")
   tela_login()

 # para sacar precisamos consultar o saldo e fazer a subtração do valor informado se estiver dentro do saldo disponível o saque será efetuado

tela_login()
janela.mainloop()