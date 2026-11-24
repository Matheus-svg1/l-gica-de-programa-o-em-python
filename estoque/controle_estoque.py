
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
    
# gerar id
def codigo_novo():

    # carrega as movimentações existentes
    gastos = dados()

    # se não houver movimentações, começa pelo ID 1
    if not gastos:
        return 1

    # pega o maior codigo e adiciona mais 1
    return max(gasto["codigo"] for gasto in gastos) +1

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
    tk.Button(janela, text="5 - Excluir Movimentação", command= excluir_movimentacao, width=25, height=2).pack(pady=7)

    #botão para gerar relatório
    tk.Button(janela, text="6 - Gerar Relatório", command= gerar_relatorio, width=25, height=2).pack(pady=7)

    #botão para sair do programa
    tk.Button(janela, text="7 - Sair", command=sair, width=25, height=2).pack(pady=7)  


# função para entradas e saídas   
def entrada_saida():
    #limpa a tela aterior
    limpar_tela()

    #texto de entradas e saídas
    tk.Label(janela, text = "Entradas e Saídas", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Label(janela, text="Código do Produto").pack()
    code = tk.Entry(janela)
    code.pack()

    

    #texto da quantidade
    tk.Label(janela, text="Quantidade").pack()

    #entry da quantidade
    quantidade = tk.Entry(janela)
    quantidade.pack()

    #selecionar tipo de movimentação
    tk.Label(janela, text="Tipo de Movimentação").pack()
    movimento = ttk.Combobox(janela, values= ["Entrada", "Saída"], state="readonly")
    movimento.pack(padx=2)

    def registrar():

        cod = code.get().strip()
        quanti = quantidade.get().strip()
        tipo = movimento.get()

        # verifica se todos os campos estão preenchidos
        if not cod or not quanti or not tipo:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # verifica se o código e a quantidade são números
        try:
            cod = int(cod)
            quant = int(quanti)
        except ValueError:
            messagebox.showerror("Erro", "Digite um código e uma quantidade válidos!")
            return

        if quant <= 0:
            messagebox.showerror("Erro", "Digite uma quantidade maior que zero!")
            return

        # carrega os dados arquivados
        lista_dados = dados()

        for item in lista_dados:

            if item["codigo"] == cod:

                if tipo == "Entrada":
                    item["quantidade"] += quant

                elif tipo == "Saída":

                    if quant > item["quantidade"]:
                        messagebox.showerror("Erro", "Estoque insuficiente")
                        return

                    item["quantidade"] -= quant

                # carrega o histórico
                historico = carregar_movimetacoes()

                nova_movimentacao = {
                    "codigo": item["codigo"],
                    "descricao": item["descricao"],
                    "tipo": tipo,
                    "quantidade": quant,
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M")
                }

                # adiciona a nova movimentação ao histórico
                historico.append(nova_movimentacao)

                # salva os arquivos
                salvar_movimentacoes(historico)
                salvar_dados(lista_dados)

                messagebox.showinfo("Sucesso", "Movimentação efetuada com sucesso!")
                menu()
                return

        messagebox.showerror("Erro", "Produto não encontrado")

    tk.Button(janela, text="Reg. Movimentação", command=registrar, width=15).pack()
    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=5)

# adicionar produto
def produto():

    #limpa a tela anterior
    limpar_tela()

    #cria o título da página
    tk.Label(janela,text="Adicionar Produto",font=("Arial", 20, "bold")).pack(pady=20)

    
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

    

        for item in lista_dados:
            if item["descricao"].lower() == nome_prod.lower():
                messagebox.showerror("Erro", "Esse produto já está cadastrado!")
                return

        # cria um novo produto caso não esteja cadastrado
        novo_produto = {
            "codigo": codigo_novo(),
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
    limpar_tela()# troca de tela

    tk.Label(janela, text="Listar Movimentações",font=("Arial", 20, "bold")).pack(pady=20)

    historico = carregar_movimetacoes() # busca o historico de transações

    if not historico:
        tk.Label(janela, text="Nenhuma Movimentação encontrada!").pack(pady=15)
    else:
        # cria a tabela
        tabela = ttk.Treeview(janela,columns=("codigo", "descricao", "tipo", "quantidade", "data"),show="headings")

        tabela.heading("codigo", text="Codigo")
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



def excluir_movimentacao():
    limpar_tela()

    tk.Label(janela, text = "Excluir Movimentação", font=("Arial", 20, "bold")).pack(pady=20)

    lista_dados = dados()
    historico = carregar_movimetacoes()

    if not historico:
        tk.Label(janela, text= "Nenhuma movimentação encontrada!").pack(pady=20)

    else:
        # cria a tabela
        tabela = ttk.Treeview(janela,columns=("codigo", "descricao", "tipo", "quantidade", "data"),show="headings")

        tabela.heading("codigo", text="Código")
        tabela.heading("descricao",text="Produto")
        tabela.heading("tipo", text="Tipo")
        tabela.heading("quantidade", text="Quantidade")
        tabela.heading("data",text="Data")

        tabela.column("codigo",width=50)
        tabela.column("descricao", width=130)
        tabela.column("tipo",width=70)
        tabela.column("quantidade", width=80)
        tabela.column("data", width=150)

        for i, item in enumerate(historico): #enumerate é um contador
            tabela.insert("", "end",iid=str(i), values=(
                item["codigo"],
                item["descricao"],
                item["tipo"],
                item["quantidade"],
                item["data"]
            ))
    tabela.pack(fill= "both", expand= True, pady =10)

    def excluir():
        selecionado = tabela.selection() #selection deixa selecionar as opções

        if not selecionado:
                messagebox.showerror("Erro", "Selecione uma movimentação!")
                return

        indice = int(selecionado[0])
        movimentacao = historico[indice]

        confirmar = messagebox.askyesno("Confirmar","Deseja realmente excluir essa movimentação?") #askyesmo é messagebox de sim ou não

        # procura o produto pelo código
        for item in lista_dados:
            if item["codigo"] == movimentacao["codigo"]:

                quantidade_inicial = item["quantidade"]

            # desfaz o efeito da movimentação excluída
                if movimentacao["tipo"] == "Entrada":
                    quantidade_inicial -= movimentacao["quantidade"]

                elif movimentacao["tipo"] == "Saída":
                    quantidade_inicial += movimentacao["quantidade"]

            item["quantidade"] = quantidade_inicial
            break

        else:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        # remove a movimentação do histórico
        historico.pop(indice)

        # salva os arquivos atualizados
        salvar_dados(lista_dados)
        salvar_movimentacoes(historico)

        messagebox.showinfo("Sucesso", "Movimentação excluída!")
        excluir_movimentacao()

    tk.Button(janela, text="Excluir Selecionada", command=excluir, width=20).pack(pady=10)

    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=5)








# função para consultar o estoque
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


# função para gerar relatório
def gerar_relatorio():

    limpar_tela()

    tk.Label(janela, text="Relatório de Estoque", font=("Arial", 20, "bold")).pack(pady=20)

    # carrega os dados
    lista_dados = dados()
    historico = carregar_movimetacoes()

    # conta os produtos e as transações
    total_produtos = len(lista_dados)
    total_transacoes = len(historico)
    estoque_baixo = 0

    # verifica quantos produtos estão no estoque mínimo
    for item in lista_dados:
        if item["quantidade"] <= item["estoque mínimo"]:
            estoque_baixo += 1

    # cria a área do relatório
    relatorio = tk.Text(janela, width=60, height=20)
    relatorio.pack(pady=10)

    # mostra o resumo
    relatorio.insert("end", "RESUMO GERAL\n") # o insert adiciona em como se fosse uma janela, ele vai juntar a string com as infiormações necesarias em cada insert
    relatorio.insert("end", "Produtos cadastrados: " + str(total_produtos) + "\n")
    relatorio.insert("end", "Total de transações: " + str(total_transacoes) + "\n")
    relatorio.insert("end", "Produtos no estoque mínimo: " + str(estoque_baixo) + "\n")

    relatorio.insert("end", "\nLISTA DE PRODUTOS\n")
    
    # mostra os produtos cadastrados
    for item in lista_dados:
        #o insert adiciona em como se fosse uma janela, ele vai juntar a string com as infiormações necesarias em cada insert
        relatorio.insert("end", "Código: " + str(item["codigo"]) + "\n")
        relatorio.insert("end", "Produto: " + item["descricao"] + "\n")
        relatorio.insert("end", "Quantidade: " + str(item["quantidade"]) + "\n")
        relatorio.insert("end", "Estoque mínimo: " + str(item["estoque mínimo"]) + "\n")
        relatorio.insert("end", "Preço: R$ " + str(item["preço"]) + "\n")

        if item["quantidade"] <= item["estoque mínimo"]:
            relatorio.insert("end", "Estado: Estoque baixo\n")
        else:
            relatorio.insert("end", "Estado: Normal\n")

        
    # impede alterações no relatório
    relatorio.config(state="disabled")

    # botão voltar
    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=10)

# função para sair
def sair():
    #messagebiox de sim ou não
    confirmar = messagebox.askyesno("Sair","Deseja realmente sair ?")

    if confirmar:
        janela.destroy()

menu()
janela.mainloop()
