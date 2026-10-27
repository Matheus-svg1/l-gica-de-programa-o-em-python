import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
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
    
'''def id_novo ():
    gastos = dados()
    if not gastos:
        return 1
    return max (gasto["id"] for gasto in gastos) +1'''


janela = tk.Tk()
janela.title("Controle de gastos")
janela.geometry("450x550")


def limpar_tela():
    for tela in janela.winfo_children(): # se tiver algo na janela do tkinter = vai ser apagado "O winfo_children guarda as informções que tem na janela"
        tela.destroy()



def menu ():
    limpar_tela()
    tk.Button(janela, text = "1 - Adicionar Receita", command= receita, width=20, height=2).pack(pady=10)
    #tk.Button(janela, text = "2 - Adicionar Despesa", command= despesa, width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "3 - Listar Movimentações", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "4 - Consultar Saldo", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "5 - Excluir Movimentação", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "6 - Gerar Relatório", width=20, height=2).pack(pady=10)
    tk.Button(janela, text = "7 - Sair", width=20, height=2).pack(pady=10)
    
    
    
def receita():
    limpar_tela()
    tk.Label(janela, text = "Receita", font=("Arial", 20, "bold")).pack(pady=20)
    
    tk.Label(janela, text = "Descrição").pack()
    descricao_receita = tk.Entry(janela)
    descricao_receita.pack()
    
    tk.Label(janela, text = "Valor ").pack()
    valor_receita = tk.Entry(janela)
    valor_receita.pack()
    def salvar_receita():
        #dado = dados
        #id_novo = len(dado) +1
        valor = valor_receita.get().strip().replace(",",".")
        descricao = descricao_receita.get()
        
        if not (valor and descricao):
            messagebox.showerror("Erro", "Preencha a descrição e o valor")
            return
        messagebox.showinfo("Sucesso", "Receita cadastrada com sucesso")
        menu()
        
        receita = {
                #"id": id_novo,
                "descricao": descricao_receita,
                "valor": valor_receita,
                "tipo": "receita",
                "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            }
            
        dado = dados()
        dado.append(receita)
        salvar_dados(dado)
        
    tk.Button(janela, text = "Enviar", command=salvar_receita, width=15).pack(pady=5)
    tk.Button(janela, text= "Voltar", width=15,command=menu).pack(pady=10),
    
    
    
'''def despesa():
    limpar_tela()
    tk.Label(janela, text = "Despesa", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(janela, text = "Descrição").pack()
    descricao_despesa = tk.Entry(janela)
    descricao_despesa.pack()
        
    tk.Label(janela, text = "Valor ").pack()
    valor_despesa = tk.Entry(janela)
    valor_despesa.pack()
    def salvar_despesa():
        valor = valor_despesa.get().strip().replace(",",".")
        descricao = descricao_despesa.get()
        
        receita = {
            "id": id_novo,
            "descricao": descricao_despesa,
            "valor": valor_despesa,
            "tipo": "despesa",
            "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        }
        dado = dados()
        dado.append(receita)
        salvar_dados(dado)
        
            
        if not(descricao and valor):
            messagebox.showerror("Erro", "Preencha a descrição e o valor")
            return
        messagebox.showinfo("Sucesso", "Sua despesa foi cadastrada com sucesso")
        menu()   
                 
    tk.Button(janela, text = "Enviar",command= salvar_despesa, width=15).pack(pady=5)
    tk.Button(janela, text= "Voltar", width=15,command=menu).pack(pady=10)'''
        

    
    
menu()   
    
janela.mainloop()