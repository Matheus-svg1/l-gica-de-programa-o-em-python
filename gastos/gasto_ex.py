from datetime import datetime
import json
import os
import tkinter as tk
from tkinter import messagebox

arquivo = "dados.json"


def dados():
    """Lê o arquivo JSON e retorna a lista de movimentações."""
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_dados(gastos):
    """Salva a lista de movimentações no arquivo JSON."""
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=4)


def id_novo():
    """Gera um novo ID incremental com base nos registros existentes."""
    gastos = dados()
    if not gastos:
        return 1
    return max(gasto["id"] for gasto in gastos) + 1


janela = tk.Tk()
janela.title("Controle de Gastos")
janela.geometry("450x550")


def limpar_tela():
    """Apaga todos os widgets da tela atual."""
    for widget in janela.winfo_children():
        widget.destroy()


def menu():
    """Exibe o menu principal."""
    limpar_tela()
    tk.Label(janela, text="Controle Financeiro", font=("Arial", 18, "bold")).pack(pady=15)

    tk.Button(janela, text="1 - Adicionar Receita", command=receita, width=22, height=2).pack(pady=5)
    tk.Button(janela, text="2 - Adicionar Despesa", command=despesa, width=22, height=2).pack(pady=5)
    tk.Button(janela, text="3 - Listar Movimentações", width=22, height=2).pack(pady=5)
    tk.Button(janela, text="4 - Consultar Saldo", width=22, height=2).pack(pady=5)
    tk.Button(janela, text="5 - Excluir Movimentação", width=22, height=2).pack(pady=5)
    tk.Button(janela, text="6 - Gerar Relatório", width=22, height=2).pack(pady=5)
    tk.Button(janela, text="7 - Sair", command=janela.quit, width=22, height=2).pack(pady=5)


def receita():
    """Interface para cadastro de receitas."""
    limpar_tela()
    tk.Label(janela, text="Receita", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Label(janela, text="Descrição").pack()
    descricao_receita = tk.Entry(janela)
    descricao_receita.pack(pady=5)

    tk.Label(janela, text="Valor (R$)").pack()
    valor_receita = tk.Entry(janela)
    valor_receita.pack(pady=5)

    def salvar_receita():
        valor_str = valor_receita.get().strip().replace(",", ".")
        descricao = descricao_receita.get().strip()

        # 1. Validação de preenchimento dos campos
        if not (valor_str and descricao):
            messagebox.showerror("Erro", "Preencha a descrição e o valor!")
            return

        # 2. Validação numérica do valor
        try:
            valor_num = float(valor_str)
            if valor_num <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que zero!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")
            return

        # 3. Criação do dicionário com os valores reais (não com os objetos Entry)
        nova_receita = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "receita",
            "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        }

        # 4. Atualização e salvamento do JSON
        lista_dados = dados()
        lista_dados.append(nova_receita)
        salvar_dados(lista_dados)

        # 5. Notificação de sucesso e redirecionamento
        messagebox.showinfo("Sucesso", "Receita cadastrada com sucesso!")
        menu()

    tk.Button(janela, text="Enviar", command=salvar_receita, width=15).pack(pady=10)
    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=5)


def despesa():
    """Interface para cadastro de despesas."""
    limpar_tela()
    tk.Label(janela, text="Despesa", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Label(janela, text="Descrição").pack()
    descricao_despesa = tk.Entry(janela)
    descricao_despesa.pack(pady=5)

    tk.Label(janela, text="Valor (R$)").pack()
    valor_despesa = tk.Entry(janela)
    valor_despesa.pack(pady=5)

    def salvar_despesa():
        valor_str = valor_despesa.get().strip().replace(",", ".")
        descricao = descricao_despesa.get().strip()

        # 1. Validação de preenchimento dos campos
        if not (valor_str and descricao):
            messagebox.showerror("Erro", "Preencha a descrição e o valor!")
            return

        # 2. Validação numérica do valor
        try:
            valor_num = float(valor_str)
            if valor_num <= 0:
                messagebox.showerror("Erro", "O valor deve ser maior que zero!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")
            return

        # 3. Criação do dicionário com os valores reais
        nova_despesa = {
            "id": id_novo(),
            "descricao": descricao,
            "valor": valor_num,
            "tipo": "despesa",
            "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        }

        # 4. Atualização e salvamento do JSON
        lista_dados = dados()
        lista_dados.append(nova_despesa)
        salvar_dados(lista_dados)

        # 5. Notificação de sucesso e redirecionamento
        messagebox.showinfo("Sucesso", "Despesa cadastrada com sucesso!")
        menu()

    tk.Button(janela, text="Enviar", command=salvar_despesa, width=15).pack(pady=10)
    tk.Button(janela, text="Voltar", command=menu, width=15).pack(pady=5)


# Inicialização da aplicação
menu()
janela.mainloop()