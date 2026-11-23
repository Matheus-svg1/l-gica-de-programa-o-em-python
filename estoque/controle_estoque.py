
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
        
        
def carregar_movimetacoes():   
    if not os.path.exists("movimentacoes.json"):
            return[]
    try:
        with open("movimentacoes.json", "r", encoding= "utf-8") as f:
            return json.load(f)
            
    except json.JSONDecodeError:
            return []


def salvar_movimentacoes(historico):
    with open("movimentacoes.json", "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii= False, indent= 4)

    
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
    tk.Button(janela, text="2 - Entradas e Saídas", command= entrada_saida, width=25, height=2).pack(pady=7)

    # botão para listar movimentações
    tk.Button(janela, text="3 - Listar Movimentações",command= listar_movimentacoes, width=25, height=2).pack(pady=7)

    #botão para consultar estoque
    tk.Button(janela, text="4 - Consultar Estoque", command= consultar_estoque, width=25, height=2).pack(pady=7)

    # botão para excluir movimentação
    tk.Button(janela, text="5 - Excluir Movimentação", width=25, height=2).pack(pady=7)

    #botão para gerar relatório
    tk.Button(janela, text="6 - Gerar Relatório", width=25, height=2).pack(pady=7)

    #botão para sair do programa
    tk.Button(janela, text="7 - Sair", width=25, height=2).pack(pady=7)  


# função para entradas e saídas   
def entrada_saida():
    #limpa a tela aterior
    limpar_tela()

    #texto de entradas e saídas
    tk.Label(janela, text = "Entradas e Saídas", font=("Arial", 20, "bold")).pack(pady=20)

    #texto do codigo do produto
    tk.Label(janela, text= "Código do Produto").pack()
    
    #entry do código
    codigo = tk.Entry(janela)
    codigo.pack()

    #texto da quantidade
    tk.Label(janela, text="Quantidade").pack()

    #entry da quantidade
    quantidade = tk.Entry(janela)
    quantidade.pack()

    #selecionar tipo de movimentação
    tk.Label(janela, text="Tipo de Movimentação").pack()
    movimento = ttk.Combobox(janela, values= ["Entrada", "Saída"], state="readonly")
    movimento.pack()

    def registrar():

        code = codigo.get().strip()
        quanti = quantidade.get().strip()
        tipo = movimento.get()

        # verifica se todos os campos estão preenchidos
        if not code or not quanti or not tipo:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        #verifica se os numeros são de 0 a 9
        if not code.isdigit() or not quanti.isdigit():
            messagebox.showerror("Erro", "Digite valores numéricos!")
            return

        cod = int(code)
        quant = int(quanti)

        if quant <=0:
            messagebox.showerror("Erro", "Digite uma quantidade maior que zero!")
            return
        #carrega os dados arquivados
        lista_dados = dados()

        for item in lista_dados:
            if item["codigo"] == cod:

                if tipo == "Entrada":
                    item ["quantidade"] +=quant

                elif tipo == "Saída":

                    if quant >  item["quantidade"]:
                        messagebox.showerror("Erro", "Estoque insuficiente")
                        return

                    item["quantidade"] -= quant


                #carregar om histórico
                historico = carregar_movimetacoes()

                nova_movimentacao = {
                "codigo": cod,
                "descricao": item["descricao"],
                "tipo": tipo,
                "quantidade": quant,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")}

                #adiciona a nova movimetação ao historico
                historico.append(nova_movimentacao)

                #salva a movimentação
                salvar_movimentacoes(historico)




                salvar_dados(lista_dados)
                messagebox.showinfo("Sucesso", "Movimentação efetuada com sucesso!")
                menu()
                return
        messagebox.showerror("Erro", "Produto não encontrado")

    tk.Button(janela, text= "Reg. Movimentação", command= registrar, width=15).pack()
    tk.Button(janela, text ="Voltar", command=menu, width=15).pack(pady=5)


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

        cod = codigo_produto.get().strip()

        # pega a quantidade digitado e troca vírgula por ponto
        quantidade = quantidade_produto.get().strip().replace(",", ".")

        # pega o preço do produto digitado
        preco_produto = preco_unidade.get().strip().replace(",",".")
        
        #pega a quantidade minima de estoque digitada
        estoque = estoque_min.get().strip()
        
        nome_prod = nome_produto.get().strip()

        cod = codigo_produto.get().strip()

        # verifica se os campos estão preenchidos
        if not cod or not quantidade or not preco_produto or not estoque or not nome_prod:
            messagebox.showerror(
                "Erro", "Preencha todos os campos!"
            )
            return

        if not cod.isdigit():
            messagebox.showerror("Erro", "Digite um código numérico!")
            return

        cod = int(cod)
        
        try:
                                             
            preco = float(preco_produto) # converte o preço para número decimal
            quant = int(quantidade) # converte a quantide para inteiro
            estoq = int(estoque) # converte o estoque para inteiro

            # verifica se o  é maior que zero
            if preco <0 or quant <0 or estoq <0:
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

        # carrega os produtos existentes
        lista_dados = dados()

        # verifica se o produto já está cadastrado
        for item in lista_dados:
            if item["codigo"] == cod:
                messagebox.showerror("Erro", "Esse código já está cadastrado!")
                return


            if item["descricao"].lower() == nome_prod.lower():

                # soma a quantidade nova com a quantidade atual
                item["quantidade"] += quant

                # atualiza o preço e o estoque mínimo
                item["preço"] = preco
                item["estoque mínimo"] = estoq

                # salva os dados atualizados
                salvar_dados(lista_dados)

                messagebox.showinfo(
                    "Sucesso",
                    "Produto já cadastrado! Quantidade e preço atualizados."
                )

                menu()
                return

        # cria um novo produto caso não esteja cadastrado
        novo_produto = {
            "codigo": cod,
            "descricao": nome_prod,
            "quantidade": quant,
            "estoque mínimo": estoq,
            "preço": preco
        }

        # adiciona o novo produto à lista
        lista_dados.append(novo_produto)

        # salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado com sucesso!"
        )

        menu()

    # botão para salvar o produto
    tk.Button(janela, text="Salvar",command=salvar_produto, width=15).pack(pady=10)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=5)


def listar_movimentacoes():
    limpar_tela()

    tk.Label(janela, text="Listar Movimentações",font=("Arial", 20, "bold")).pack(pady=20)

    historico = carregar_movimetacoes()

    if not historico:
        tk.Label(janela, text="Nenhuma Movimentação encontrada!").pack(pady=15)
    else:
        # cria a tabela
        tabela = ttk.Treeview(
            janela,
            columns=("codigo", "descricao", "tipo", "quantidade", "data"),
            show="headings"
        )

        tabela.heading("codigo", text="Código")
        tabela.heading("descricao", text="Produto")
        tabela.heading("tipo", text="Tipo")
        tabela.heading("quantidade", text="Quantidade")
        tabela.heading("data", text="Data")

        # largura das colunas
        tabela.column("codigo", width=50)
        tabela.column("descricao", width=130)
        tabela.column("tipo", width=70)
        tabela.column("quantidade", width=80)
        tabela.column("data", width=150)


        for item in historico:
            tabela.insert("", "end", values=(item["codigo"],item["descricao"],item["tipo"],item["quantidade"],item["data"]))

        tabela.pack(pady=10, fill="both", expand=True)

    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=10)


def consultar_estoque():

    limpar_tela()


    tk.Label(janela, text="Consultar estoque",font=("Arial", 20, "bold")).pack(pady=20)
    lista_dados = dados()
    print(lista_dados)
    print(os.path.abspath(arquivo))

    if not lista_dados:
        tk.Label(janela, text="Nenhum produto encontrado!").pack(pady=15)   
    else:
        # cria a tabela
        tabela = ttk.Treeview(janela,columns=("codigo", "descricao", "quantidade", "minimo","preco", "estado"),show="headings")

        # nomes das colunas
        tabela.heading("codigo", text="Código")
        tabela.heading("descricao", text="Produto")
        tabela.heading("quantidade", text="Qtd.")
        tabela.heading("minimo", text="Mínimo")
        tabela.heading("preco", text="Preço")
        tabela.heading("estado", text="Estado")

        # largura das colunas
        tabela.column("codigo", width=50)
        tabela.column("descricao", width=120)
        tabela.column("quantidade", width=55)
        tabela.column("minimo", width=55)
        tabela.column("preco", width=80)
        tabela.column("estado", width=100)

        for item in lista_dados:

            # verifica se o estoque está baixo
            if item["quantidade"] <= item["estoque mínimo"]:
                estado = "Estoque baixo"
            else:
                estado = "Normal"

            # adiciona o produto na tabela
            tabela.insert("", "end", values=(
                item["codigo"],
                item["descricao"],
                item["quantidade"],
                item["estoque mínimo"],
                f"R$ {float(item['preço']):.2f}",
                estado
            ))

        tabela.pack(pady=10, fill="both", expand=True)

    # botão voltar
    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=10)

menu()
janela.mainloop()
