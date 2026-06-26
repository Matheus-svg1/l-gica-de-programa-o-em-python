def desenha_linha(limite, preenchimento, largura):
    print(limite + preenchimento * (largura - 2) + limite)

def montar_menu(itens, largura):
    desenha_linha('+', '-', largura)

    espaco = largura - 4  # desconta "| " e " |"

    for item in itens:
        print(f'| {item:<{espaco}} |')
        if item != itens[-1]:
            desenha_linha('+', '-', largura)

    desenha_linha('+', '-', largura)

itens = ['Usuários', 'Clientes', 'Fornecedores', 'Relatórios']
montar_menu(itens, 24)