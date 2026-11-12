import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk
import json
import os
from datetime import datetime

janela = tk.Tk()
janela.geometry("550x600")
janela.title("Controle de Estoque")

arquivo = "banco.json"

def dados():
    if not os.path.exists(arquivo):
        return[]
    try:
        with open(arquivo, "r", encoding= "utf-8") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []
    
    
def salvar_dados(estoque):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii= False, indent= 4)
        
        
    

# gerar id
def codigo_novo():

    # carrega as movimentações existentes
    gastos = dados()

    # se não houver movimentações, começa pelo ID 1
    if not gastos:
        return 0

    # pega o maior codigo e adiciona mais 1
    return max(gasto["codigo"] for gasto in gastos) +1



    
 # limppar tela
def limpar_tela():

    # percorre todos os elementos da janela
    for tela in janela.winfo_children():

        # tira o que tem na tela
        tela.destroy()


# memu principal
def menu():

    # limpa a tela anterior
    limpar_tela()

    # cria o título do sistema
    tk.Label(janela, text="Controle de Estoque", font=("Arial", 20, "bold")).pack(pady=15)

    #botão para adicionar produto
    tk.Button(janela, text="1 - Adicionar Produto", command= produto, width=25, height=2).pack(pady=7)

    # botão para entradas e saídas
    tk.Button(janela, text="2 - Entradas e Saídas", width=25, height=2).pack(pady=7)

    # botão para listar movimentações
    tk.Button(janela, text="3 - Listar Movimentações", width=25, height=2).pack(pady=7)

    #botão para consultar estoque
    tk.Button(janela, text="4 - Consultar Estoque", width=25, height=2).pack(pady=7)

    # botão para excluir movimentação
    tk.Button(janela, text="5 - Excluir Movimentação", width=25, height=2).pack(pady=7)

    #botão para gerar relatório
    tk.Button(janela, text="6 - Gerar Relatório", width=25, height=2).pack(pady=7)

    #botão para sair do programa
    tk.Button(janela, text="7 - Sair", width=25, height=2).pack(pady=7)  
    
    
    
    
# adicionar produto
def produto():

    #limpa a tela anterior
    limpar_tela()

    #cria o título da página
    tk.Label(janela,text="Adicionar Produto",font=("Arial", 20, "bold")).pack(pady=20)

    #texto do códigpo do produto
    tk.Label(janela, text = "Código").pack()
    
    #entry do código do produto
    codigo_produto = tk.Entry(janela)
    codigo_produto.pack()
    
    # texto de nome do produto
    tk.Label(janela, text="Nome do produto").pack()

    # entry da descrição
    nome_produto = tk.Entry(janela)
    nome_produto.pack()

    # texto da quantidade
    tk.Label(janela, text="Quantidade").pack()

    # entry da quantidade
    quantidade_produto = tk.Entry(janela)
    quantidade_produto.pack()
    
    # texto do estoque mínimo
    tk.Label(janela, text = "Estoque Mínimo").pack()
    
    #entry do estoque mínimo
    estoque_min = tk.Entry(janela)
    estoque_min.pack()
    
    #texto do preço por unidade
    tk.Label(janela, text = "Preço Unitário").pack()
    
    #entry do preço por unidade
    preco_unidade = tk.Entry(janela)
    preco_unidade.pack()
    

    # função responsável por salvar a receita
    def salvar_produto():

        # pega a quantidade digitado e troca vírgula por ponto
        quantidade = quantidade_produto.get().strip().replace(",", ".")

        # pega o preço do produto digitado
        preco_produto = preco_unidade.get().strip().replace(",",".")
        
        #pega a quantidade minima de estoque digitada
        estoque = estoque_min.get().strip()
        
        nome_prod = nome_produto.get().strip()

        # verifica se os campos estão preenchidos
        if not quantidade or not preco_produto or not estoque or not nome_prod:
            messagebox.showerror(
                "Erro", "Preencha todos os campos!"
            )
            return

        try:
                                             
            preco = float(preco_produto) # converte o preço para número decimal
            quant = int(quantidade) # converte a quantide para inteiro
            estoq = int(estoque) # converte o estoque para inteiro

            # verifica se o  é maior que zero
            if preco <=0 or quant <=0 or estoq <=0:
                messagebox.showerror(
                    "Erro", "O valor deve ser maior que zero!"
                )
                return

        # trata erros caso o valor não seja numérico
        except ValueError:
            messagebox.showerror(
                "Erro", "Digite um valor numérico válido!"
            )
            return

        # cria um dicionário com os dados da receita
        novo_produto = {
            "codigo":codigo_novo(),
            "descricao": nome_prod,
            "quantidade":quant,
            "estoque mínimo":estoq,
            "valor": preco,
            

            # registra a data e a hora atuais
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # carrega as movimentações existentes
        lista_dados = dados()

        # adiciona a nova receita à lista
        lista_dados.append(novo_produto)

        # salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        # menssagebox de sucesso
        messagebox.showinfo(
            "Sucesso", "Receita cadastrada com sucesso!"
        )

        # chama o menu
        menu()

        # botão para salvar o produto
    tk.Button(janela, text="Salvar",command=salvar_produto, width=15).pack(pady=10)

        # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=5)
    
    
    
    
    
    
    
    
menu()
janela.mainloop()
