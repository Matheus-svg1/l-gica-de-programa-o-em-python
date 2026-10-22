import tkinter as tk
from tkinter import messagebox
import json
import os

arquivo = "dados.json"

def dados():
    if not os.path.exists(arquivo):
        return[]
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]
    
def salvar_dados(gastos):
    with open(arquivo, "w", encoding= "utf-8") as f:
        json.dump(gastos, f, ensure_ascii= False, indent=4)
    


janela = tk.Tk()
janela.title("Controle de gastos")
janela.geometry("450x550")


def limpar_tela():
    for tela in janela.winfo_children(): # se tiver algo na janela do tkinter = vai ser apagado "O winfo_children guarda as informções que tem na janela"
        tela.destroy()



def menu ():
    limpar_tela()
    tk.Button(janela, text = "1 - Adicionar Receita", command= receita, width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "2 - Adicionar Despesa", command= despesa, width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "3 - Listar Movimentações", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "4 - Consultar Saldo", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "5 - Excluir Movimentação", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "6 - Gerar Relatório", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "7 - Sair", width=20, height=2).pack(pady=10)
    
    

        
    
    
def receita():
    limpar_tela()
    tk.Label(janela, text = "Receita", font=("Arial", 20, "bold")).pack(pady=20)
    
    tk.Label(janela, text = "Descrição").pack()
    descricao = tk.Entry(janela)
    descricao.pack()
    
    tk.Label(janela, text = "Valor ").pack()
    valor = tk.Entry(janela)
    valor.pack()
    
    tk.Button(janela, text = "Enviar", width=15).pack(pady=5)
    
    
def despesa():
    limpar_tela()
    tk.Label(janela, text = "Despesa", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(janela, text = "Descrição").pack()
    descricao = tk.Entry(janela)
    descricao.pack()
        
    tk.Label(janela, text = "Valor ").pack()
    valor = tk.Entry(janela)
    valor.pack()
        
    tk.Button(janela, text = "Enviar", width=15).pack(pady=5)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
menu()   
    
janela.mainloop()