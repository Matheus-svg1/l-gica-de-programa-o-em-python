import tkinter as tk  
from tkinter import messagebox  
from tkinter import ttk  # tabelas
import json  #  arquivos JSON
import os  # verifica arquivos no computador
from datetime import datetime  #data e hora

# nome do arquivo onde os dados serão salvos
arquivo = "dados.json"


# carregar dados
def dados():

    # verifica se o arquivo existe
    if not os.path.exists(arquivo):
        return []

    try:
        # abre o arquivo para leitura
        with open(arquivo, "r", encoding="utf-8") as f:

            # carrega os dados do JSON
            return json.load(f)

    # trata erros caso o JSON esteja inválido
    except json.JSONDecodeError:
        return []


# salvar dados
def salvar_dados(gastos):

    # abre o arquivo para escrita
    with open(arquivo, "w", encoding="utf-8") as f:

        # salva os dados no formato JSON
        json.dump(gastos, f, ensure_ascii=False, indent=4)


# gerar id
def id_novo():

    # carrega as movimentações existentes
    gastos = dados()

    # se não houver movimentações, começa pelo ID 1
    if not gastos:
        return 1

    # pega o maior ID e adiciona mais 1
    return max(gasto["id"] for gasto in gastos) + 1


janela = tk.Tk()
janela.title("Controle de Gastos")
janela.geometry("600x550")


# limppar tela
def limpar_tela():

    # percorre todos os elementos da janela
    for tela in janela.winfo_children():

        # remove os elementos da tela
        tela.destroy()


# memu principal
def menu():

    # limpa a tela anterior
    limpar_tela()

    # Cria o título do sistema
    tk.Label(janela, text="Controle Financeiro", font=("Arial", 20, "bold")).pack(pady=15)

    # Botão para adicionar receita
    tk.Button(janela, text="1 - Adicionar Receita",command=receita, width=25, height=2).pack(pady=7)

    # Botão para adicionar despesa
    tk.Button(janela, text="2 - Adicionar Despesa",command=despesa, width=25, height=2).pack(pady=7)

    # Botão para listar movimentações
    tk.Button(janela, text="3 - Listar Movimentações",command=movimentacoes, width=25, height=2).pack(pady=7)

    # Botão para consultar saldo
    tk.Button(janela, text="4 - Consultar Saldo",command=consultar_saldo, width=25, height=2).pack(pady=7)

    # Botão para excluir movimentação
    tk.Button(janela, text="5 - Excluir Movimentação",command=excluir_movimentacao, width=25, height=2).pack(pady=7)

    # Botão para gerar relatório
    tk.Button(janela, text="6 - Gerar Relatório",command=relatorio, width=25, height=2).pack(pady=7)

    # Botão para sair do programa
    tk.Button(janela, text="7 - Sair",command=sair, width=25, height=2).pack(pady=7)


# adicionar receita
def receita():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título da página
    tk.Label(janela,text="Adicionar Receita",font=("Arial", 20, "bold")).pack(pady=20)

    # Campo para informar a descrição
    tk.Label(janela, text="Descrição").pack()

    # Cria o campo de texto da descrição
    descricao_receita = tk.Entry(janela)
    descricao_receita.pack()

    # Campo para informar o valor
    tk.Label(janela, text="Valor").pack()

    # Cria o campo de texto do valor
    valor_receita = tk.Entry(janela)
    valor_receita.pack()

    # função responsável por salvar a receita
    def salvar_receita():

        # pega o valor digitado e troca vírgula por ponto
        valor = valor_receita.get().strip().replace(",", ".")

        # pega a descrição digitada
        descricao = descricao_receita.get().strip()

        # verifica se os campos estão preenchidos
        if not valor or not descricao:
            messagebox.showerror(
                "Erro", "Preencha a descrição e o valor!"
            )
            return

        try:
            # converte o valor para número decimal
            valor_num = float(valor)

            # verifica se o valor é maior que zero
            if valor_num <= 0:
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
        nova_receita = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "receita",

            # registra a data e a hora atuais
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # carrega as movimentações existentes
        lista_dados = dados()

        # adiciona a nova receita à lista
        lista_dados.append(nova_receita)

        # salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        # exibe mensagem de sucesso
        messagebox.showinfo(
            "Sucesso", "Receita cadastrada com sucesso!"
        )

        # Volta ao menu principal
        menu()

    # botão para salvar a receita
    tk.Button(janela, text="Salvar",command=salvar_receita, width=15).pack(pady=10)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=5)


# adicionar despesa
def despesa():

    # limpa a tela anterior
    limpar_tela()

    # cria o título da página
    tk.Label(janela,text="Adicionar Despesa",font=("Arial", 20, "bold")).pack(pady=20)

    # campo para informar a descrição
    tk.Label(janela, text="Descrição").pack()

    # cria o campo de texto da descrição
    descricao_despesa = tk.Entry(janela)
    descricao_despesa.pack()

    # campo para informar o valor
    tk.Label(janela, text="Valor").pack()

    # cria o campo de texto do valor
    valor_despesa = tk.Entry(janela)
    valor_despesa.pack()

    # função responsável por salvar a despesa
    def salvar_despesa():

        # pega o valor digitado e troca vírgula por ponto
        valor = valor_despesa.get().strip().replace(",", ".")

        # pega a descrição digitada
        descricao = descricao_despesa.get().strip()

        # verifica se os campos estão preenchidos
        if not valor or not descricao:
            messagebox.showerror(
                "Erro", "Preencha a descrição e o valor!"
            )
            return

        try:
            # converte o valor para número decimal
            valor_num = float(valor)

            # verifica se o valor é maior que zero
            if valor_num <= 0:
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

        # cria um dicionário com os dados da despesa
        nova_despesa = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "despesa",

            # registra a data e a hora atuais
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # carrega as movimentações existentes
        lista_dados = dados()

        # adiciona a nova despesa à lista
        lista_dados.append(nova_despesa)

        # salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        # exibe mensagem de sucesso
        messagebox.showinfo(
            "Sucesso", "Despesa cadastrada com sucesso!"
        )

        # volta ao menu principal
        menu()

    # botão para salvar a despesa
    tk.Button(
        janela, text="Salvar",
        command=salvar_despesa, width=15
    ).pack(pady=10)

    # botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=5)


# listar movimentações
def movimentacoes():

    # limpa a tela anterior
    limpar_tela()

    # cria o título da página
    tk.Label(
        janela,
        text="Movimentações",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # cria uma tabela com as colunas
    tabela = ttk.Treeview(
        janela,
        columns=("ID", "Descricao", "Valor", "Tipo", "Data"),
        show="headings"
    )

    # define os títulos das colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Descricao", text="Descrição")
    tabela.heading("Valor", text="Valor")
    tabela.heading("Tipo", text="Tipo")
    tabela.heading("Data", text="Data/Hora")

    # define a largura e o alinhamento das colunas
    tabela.column("ID", width=35, anchor="center")
    tabela.column("Descricao", width=110, anchor="center")
    tabela.column("Valor", width=90, anchor="center")
    tabela.column("Tipo", width=75, anchor="center")
    tabela.column("Data", width=150, anchor="center")

    # carrega as movimentações salvas
    lista_dados = dados()

    # percorre todas as movimentações
    for gasto in lista_dados:

        # insere cada movimentação na tabela
        tabela.insert(
            "",
            "end",
            values=(
                gasto["id"],
                gasto["descricao"],
                f"R$ {gasto['valor']:.2f}",

                # deixa a primeira letra maiúscula
                gasto["tipo"].capitalize(),
                gasto["data"]
            )
        )

    # exibe a tabela na janela
    tabela.pack(pady=10)

    # verifica se não existem movimentações
    if not lista_dados:
        tk.Label(
            janela,
            text="Nenhuma movimentação cadastrada."
        ).pack(pady=5)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=15)


# consultar saldo
def consultar_saldo():

    # limpa a tela anterior
    limpar_tela()

    # carrega as movimentações
    lista_dados = dados()

    # soma todos os valores das receitas
    receitas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "receita"
    )

    # soma todos os valores das despesas
    despesas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "despesa"
    )

    # calcula o saldo subtraindo as despesas das receitas
    saldo = receitas - despesas

    # mostra o título da página
    tk.Label(janela,text="Saldo Financeiro",font=("Arial", 20, "bold")).pack(pady=25)

    # mostra o total de receitas
    tk.Label(janela,text=f"Receitas: R$ {receitas:.2f}",font=("Arial", 14)).pack(pady=10)

    # mostra o total de despesas
    tk.Label(janela,text=f"Despesas: R$ {despesas:.2f}",font=("Arial", 14)).pack(pady=10)

    # mostra o saldo atual
    tk.Label(janela,text=f"Saldo atual: R$ {saldo:.2f}",font=("Arial", 16, "bold")).pack(pady=20)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=10)


# executar movimentação
def excluir_movimentacao():

    # limpa a tela anterior
    limpar_tela()

    # cria o título da página
    tk.Label(janela,text="Excluir Movimentação",font=("Arial", 20, "bold")).pack(pady=20)

    # solicita o ID da movimentação
    tk.Label(janela,text="Digite o ID da movimentação:").pack()

    # campo para digitar o ID
    id_excluir = tk.Entry(janela)
    id_excluir.pack(pady=10)

    # função responsável por excluir
    def excluir():

        #pega o ID digitado
        identificador = id_excluir.get().strip()

        # verifica se o campo está vazio
        if not identificador:
            messagebox.showerror("Erro", "Informe o ID!")
            return

        try:
            # converte o ID para número inteiro
            identificador = int(identificador)

        # trata erros caso o ID não seja numérico
        except ValueError:
            messagebox.showerror(
                "Erro", "Digite um ID válido!"
            )
            return

        # carrega as movimentações
        lista_dados = dados()

        # percorre todas as movimentações
        for gasto in lista_dados:

            # verifica se encontrou o ID informado
            if gasto["id"] == identificador:

                # pergunta se o usuário confirma a exclusão
                confirmar = messagebox.askyesno(
                    "Confirmar exclusão",
                    f"Deseja excluir {gasto['descricao']}?"
                )

                # executa a exclusão se confirmado
                if confirmar:

                    # remove a movimentação da lista
                    lista_dados.remove(gasto)

                    # salva a lista atualizada no JSON
                    salvar_dados(lista_dados)

                    # exibe mensagem de sucesso
                    messagebox.showinfo(
                        "Sucesso",
                        "Movimentação excluída com sucesso!"
                    )

                    # volta ao menu principal
                    menu()

                return

        # mostra erro se o ID não for encontrado
        messagebox.showerror(
            "Erro", "Movimentação não encontrada!"
        )

    # botão para excluir
    tk.Button(janela, text="Excluir",command=excluir, width=15).pack(pady=10)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=10)


# gerar relatório
def relatorio():

    #limpa a tela anterior
    limpar_tela()

    # carrega as movimentações
    lista_dados = dados()

    # soma todas as receitas
    receitas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "receita"
    )

    # soma todas as despesas
    despesas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "despesa"
    )

    # calcula o saldo atual
    saldo = receitas - despesas

    # conta a quantidade de movimentações
    quantidade = len(lista_dados)

    # mostra o título do relatório
    tk.Label(janela,text="Relatório Financeiro",font=("Arial", 20, "bold")).pack(pady=25)

    # mostra o total de receitas
    tk.Label(janela,text=f"Total de receitas: R$ {receitas:.2f}",font=("Arial", 13)).pack(pady=10)

    # mostra o total de despesas
    tk.Label(janela,text=f"Total de despesas: R$ {despesas:.2f}",font=("Arial", 13)).pack(pady=10)

    # mostra o saldo atual
    tk.Label(janela,text=f"Saldo atual: R$ {saldo:.2f}",font=("Arial", 15, "bold")).pack(pady=10)

    # mostra a quantidade de movimentações
    tk.Label(janela,text=f"Quantidade de movimentações: {quantidade}",font=("Arial", 13)).pack(pady=10)

    # botão para voltar ao menu
    tk.Button(janela, text="Voltar",command=menu, width=15).pack(pady=20)


# sair
def sair():

    # mensagebox de sim ou não
    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair do programa?"
    )

    # fecha a janela se o usuário confirmar
    if resposta:
        janela.destroy()




# abre o menu principal
menu()


janela.mainloop()
