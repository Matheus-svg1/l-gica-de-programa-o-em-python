
# IMPORTAR BIBLIOTECAS

import tkinter as tk  # Cria a interface gráfica
from tkinter import messagebox  # Exibe mensagens na tela
from tkinter import ttk  # Cria tabelas
import json  # Trabalha com arquivos JSON
import os  # Verifica arquivos no computador
from datetime import datetime  # Trabalha com data e hora

# Nome do arquivo onde os dados serão salvos
arquivo = "dados.json"


# CARREGAR DADOS
def dados():

    # Verifica se o arquivo existe
    if not os.path.exists(arquivo):
        return []

    try:
        # Abre o arquivo para leitura
        with open(arquivo, "r", encoding="utf-8") as f:

            # Carrega os dados do JSON
            return json.load(f)

    # Trata erros caso o JSON esteja inválido
    except json.JSONDecodeError:
        return []


# SALVAR DADOS
def salvar_dados(gastos):

    # Abre o arquivo para escrita
    with open(arquivo, "w", encoding="utf-8") as f:

        # Salva os dados no formato JSON
        json.dump(gastos, f, ensure_ascii=False, indent=4)


# GERAR ID
def id_novo():

    # Carrega as movimentações existentes
    gastos = dados()

    # Se não houver movimentações, começa pelo ID 1
    if not gastos:
        return 1

    # Pega o maior ID e adiciona mais 1
    return max(gasto["id"] for gasto in gastos) + 1


# JANELA PRINCIPAL

# Cria a janela do programa
janela = tk.Tk()

# Define o título da janela
janela.title("Controle de Gastos")

# Define o tamanho da janela
janela.geometry("600x550")


# LIMPAR TELA
def limpar_tela():

    # Percorre todos os elementos da janela
    for tela in janela.winfo_children():

        # Remove os elementos da tela
        tela.destroy()


# MENU PRINCIPAL
def menu():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título do sistema
    tk.Label(
        janela,
        text="Controle Financeiro",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    # Botão para adicionar receita
    tk.Button(
        janela, text="1 - Adicionar Receita",
        command=receita, width=25, height=2
    ).pack(pady=7)

    # Botão para adicionar despesa
    tk.Button(
        janela, text="2 - Adicionar Despesa",
        command=despesa, width=25, height=2
    ).pack(pady=7)

    # Botão para listar movimentações
    tk.Button(
        janela, text="3 - Listar Movimentações",
        command=movimentacoes, width=25, height=2
    ).pack(pady=7)

    # Botão para consultar saldo
    tk.Button(
        janela, text="4 - Consultar Saldo",
        command=consultar_saldo, width=25, height=2
    ).pack(pady=7)

    # Botão para excluir movimentação
    tk.Button(
        janela, text="5 - Excluir Movimentação",
        command=excluir_movimentacao, width=25, height=2
    ).pack(pady=7)

    # Botão para gerar relatório
    tk.Button(
        janela, text="6 - Gerar Relatório",
        command=relatorio, width=25, height=2
    ).pack(pady=7)

    # Botão para sair do programa
    tk.Button(
        janela, text="7 - Sair",
        command=sair, width=25, height=2
    ).pack(pady=7)


# ADICIONAR RECEITA
def receita():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título da página
    tk.Label(
        janela,
        text="Adicionar Receita",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

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

    # Função responsável por salvar a receita
    def salvar_receita():

        # Pega o valor digitado e troca vírgula por ponto
        valor = valor_receita.get().strip().replace(",", ".")

        # Pega a descrição digitada
        descricao = descricao_receita.get().strip()

        # Verifica se os campos estão preenchidos
        if not valor or not descricao:
            messagebox.showerror(
                "Erro", "Preencha a descrição e o valor!"
            )
            return

        try:
            # Converte o valor para número decimal
            valor_num = float(valor)

            # Verifica se o valor é maior que zero
            if valor_num <= 0:
                messagebox.showerror(
                    "Erro", "O valor deve ser maior que zero!"
                )
                return

        # Trata erros caso o valor não seja numérico
        except ValueError:
            messagebox.showerror(
                "Erro", "Digite um valor numérico válido!"
            )
            return

        # Cria um dicionário com os dados da receita
        nova_receita = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "receita",

            # Registra a data e a hora atuais
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # Carrega as movimentações existentes
        lista_dados = dados()

        # Adiciona a nova receita à lista
        lista_dados.append(nova_receita)

        # Salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        # Exibe mensagem de sucesso
        messagebox.showinfo(
            "Sucesso", "Receita cadastrada com sucesso!"
        )

        # Volta ao menu principal
        menu()

    # Botão para salvar a receita
    tk.Button(
        janela, text="Salvar",
        command=salvar_receita, width=15
    ).pack(pady=10)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=5)


# ADICIONAR DESPESA
def despesa():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título da página
    tk.Label(
        janela,
        text="Adicionar Despesa",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Campo para informar a descrição
    tk.Label(janela, text="Descrição").pack()

    # Cria o campo de texto da descrição
    descricao_despesa = tk.Entry(janela)
    descricao_despesa.pack()

    # Campo para informar o valor
    tk.Label(janela, text="Valor").pack()

    # Cria o campo de texto do valor
    valor_despesa = tk.Entry(janela)
    valor_despesa.pack()

    # Função responsável por salvar a despesa
    def salvar_despesa():

        # Pega o valor digitado e troca vírgula por ponto
        valor = valor_despesa.get().strip().replace(",", ".")

        # Pega a descrição digitada
        descricao = descricao_despesa.get().strip()

        # Verifica se os campos estão preenchidos
        if not valor or not descricao:
            messagebox.showerror(
                "Erro", "Preencha a descrição e o valor!"
            )
            return

        try:
            # Converte o valor para número decimal
            valor_num = float(valor)

            # Verifica se o valor é maior que zero
            if valor_num <= 0:
                messagebox.showerror(
                    "Erro", "O valor deve ser maior que zero!"
                )
                return

        # Trata erros caso o valor não seja numérico
        except ValueError:
            messagebox.showerror(
                "Erro", "Digite um valor numérico válido!"
            )
            return

        # Cria um dicionário com os dados da despesa
        nova_despesa = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "despesa",

            # Registra a data e a hora atuais
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        # Carrega as movimentações existentes
        lista_dados = dados()

        # Adiciona a nova despesa à lista
        lista_dados.append(nova_despesa)

        # Salva os dados atualizados no JSON
        salvar_dados(lista_dados)

        # Exibe mensagem de sucesso
        messagebox.showinfo(
            "Sucesso", "Despesa cadastrada com sucesso!"
        )

        # Volta ao menu principal
        menu()

    # Botão para salvar a despesa
    tk.Button(
        janela, text="Salvar",
        command=salvar_despesa, width=15
    ).pack(pady=10)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=5)


# LISTAR MOVIMENTAÇÕES EM TABELA
def movimentacoes():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título da página
    tk.Label(
        janela,
        text="Movimentações",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Cria uma tabela com as colunas
    tabela = ttk.Treeview(
        janela,
        columns=("ID", "Descricao", "Valor", "Tipo", "Data"),
        show="headings"
    )

    # Define os títulos das colunas
    tabela.heading("ID", text="ID")
    tabela.heading("Descricao", text="Descrição")
    tabela.heading("Valor", text="Valor")
    tabela.heading("Tipo", text="Tipo")
    tabela.heading("Data", text="Data/Hora")

    # Define a largura e o alinhamento das colunas
    tabela.column("ID", width=35, anchor="center")
    tabela.column("Descricao", width=110, anchor="center")
    tabela.column("Valor", width=90, anchor="center")
    tabela.column("Tipo", width=75, anchor="center")
    tabela.column("Data", width=150, anchor="center")

    # Carrega as movimentações salvas
    lista_dados = dados()

    # Percorre todas as movimentações
    for gasto in lista_dados:

        # Insere cada movimentação na tabela
        tabela.insert(
            "",
            "end",
            values=(
                gasto["id"],
                gasto["descricao"],
                f"R$ {gasto['valor']:.2f}",

                # Deixa a primeira letra maiúscula
                gasto["tipo"].capitalize(),
                gasto["data"]
            )
        )

    # Exibe a tabela na janela
    tabela.pack(pady=10)

    # Verifica se não existem movimentações
    if not lista_dados:
        tk.Label(
            janela,
            text="Nenhuma movimentação cadastrada."
        ).pack(pady=5)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=15)


# CONSULTAR SALDO
def consultar_saldo():

    # Limpa a tela anterior
    limpar_tela()

    # Carrega as movimentações
    lista_dados = dados()

    # Soma todos os valores das receitas
    receitas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "receita"
    )

    # Soma todos os valores das despesas
    despesas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "despesa"
    )

    # Calcula o saldo subtraindo as despesas das receitas
    saldo = receitas - despesas

    # Mostra o título da página
    tk.Label(
        janela,
        text="Saldo Financeiro",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    # Mostra o total de receitas
    tk.Label(
        janela,
        text=f"Receitas: R$ {receitas:.2f}",
        font=("Arial", 14)
    ).pack(pady=10)

    # Mostra o total de despesas
    tk.Label(
        janela,
        text=f"Despesas: R$ {despesas:.2f}",
        font=("Arial", 14)
    ).pack(pady=10)

    # Mostra o saldo atual
    tk.Label(
        janela,
        text=f"Saldo atual: R$ {saldo:.2f}",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=10)


# EXCLUIR MOVIMENTAÇÃO
def excluir_movimentacao():

    # Limpa a tela anterior
    limpar_tela()

    # Cria o título da página
    tk.Label(
        janela,
        text="Excluir Movimentação",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # Solicita o ID da movimentação
    tk.Label(
        janela,
        text="Digite o ID da movimentação:"
    ).pack()

    # Campo para digitar o ID
    id_excluir = tk.Entry(janela)
    id_excluir.pack(pady=10)

    # Função responsável por excluir
    def excluir():

        # Pega o ID digitado
        identificador = id_excluir.get().strip()

        # Verifica se o campo está vazio
        if not identificador:
            messagebox.showerror("Erro", "Informe o ID!")
            return

        try:
            # Converte o ID para número inteiro
            identificador = int(identificador)

        # Trata erros caso o ID não seja numérico
        except ValueError:
            messagebox.showerror(
                "Erro", "Digite um ID válido!"
            )
            return

        # Carrega as movimentações
        lista_dados = dados()

        # Percorre todas as movimentações
        for gasto in lista_dados:

            # Verifica se encontrou o ID informado
            if gasto["id"] == identificador:

                # Pergunta se o usuário confirma a exclusão
                confirmar = messagebox.askyesno(
                    "Confirmar exclusão",
                    f"Deseja excluir {gasto['descricao']}?"
                )

                # Executa a exclusão se confirmado
                if confirmar:

                    # Remove a movimentação da lista
                    lista_dados.remove(gasto)

                    # Salva a lista atualizada no JSON
                    salvar_dados(lista_dados)

                    # Exibe mensagem de sucesso
                    messagebox.showinfo(
                        "Sucesso",
                        "Movimentação excluída com sucesso!"
                    )

                    # Volta ao menu principal
                    menu()

                return

        # Mostra erro se o ID não for encontrado
        messagebox.showerror(
            "Erro", "Movimentação não encontrada!"
        )

    # Botão para excluir
    tk.Button(
        janela, text="Excluir",
        command=excluir, width=15
    ).pack(pady=10)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=10)


# GERAR RELATÓRIO
def relatorio():

    # Limpa a tela anterior
    limpar_tela()

    # Carrega as movimentações
    lista_dados = dados()

    # Soma todas as receitas
    receitas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "receita"
    )

    # Soma todas as despesas
    despesas = sum(
        gasto["valor"]
        for gasto in lista_dados
        if gasto["tipo"] == "despesa"
    )

    # Calcula o saldo atual
    saldo = receitas - despesas

    # Conta a quantidade de movimentações
    quantidade = len(lista_dados)

    # Mostra o título do relatório
    tk.Label(
        janela,
        text="Relatório Financeiro",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    # Mostra o total de receitas
    tk.Label(
        janela,
        text=f"Total de receitas: R$ {receitas:.2f}",
        font=("Arial", 13)
    ).pack(pady=10)

    # Mostra o total de despesas
    tk.Label(
        janela,
        text=f"Total de despesas: R$ {despesas:.2f}",
        font=("Arial", 13)
    ).pack(pady=10)

    # Mostra o saldo atual
    tk.Label(
        janela,
        text=f"Saldo atual: R$ {saldo:.2f}",
        font=("Arial", 15, "bold")
    ).pack(pady=10)

    # Mostra a quantidade de movimentações
    tk.Label(
        janela,
        text=f"Quantidade de movimentações: {quantidade}",
        font=("Arial", 13)
    ).pack(pady=10)

    # Botão para voltar ao menu
    tk.Button(
        janela, text="Voltar",
        command=menu, width=15
    ).pack(pady=20)


# SAIR
def sair():

    # Pergunta se o usuário deseja sair
    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair do programa?"
    )

    # Fecha a janela se o usuário confirmar
    if resposta:
        janela.destroy()


# INICIAR PROGRAMA

# Abre o menu principal
menu()

# Mantém a janela funcionando
janela.mainloop()
