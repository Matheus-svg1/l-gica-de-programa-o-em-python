import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Caixa eletrônico")
janela.geometry("600x750")

tk.Label(janela, text = "Bem-vindo ao Caixa Eletrônico!!").grid(row = )
saldo_inicial = 1000

tk.Label(janela, text = "Digite a sua conta").grid(row = 1, column= 0)
conta = tk.Entry(janela, text = "")
conta.grid(row =1, column=0)
def menu ():
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print(" 4 - Sair")

    opcao = input("Escolha uma opção !")
    menu()

    if opcao == "0":
        pass




janela.mainloop()