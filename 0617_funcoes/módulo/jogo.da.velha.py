
linhas = 3
colunas = 3
jogador= "X"
tabuleiro = []

for p in range(linhas):
    linha = []
    for g in range(colunas):
        linha.append(" ")
    tabuleiro.append(linha)
while True:
    coluna_escolhida = int(input("Escolha uma coluna de (0 a 2): "))
    linha_escolhida = int(input("Escolha uma linha de (0 a 2): "))
    if linha_escolhida < 0 or linha_escolhida > 2 or coluna_escolhida < 0 or coluna_escolhida >2:
        print("Posição inválida!")
    if  tabuleiro[linha_escolhida][coluna_escolhida] == " ":
        tabuleiro[linha_escolhida][coluna_escolhida] = jogador
    else:
        print("Esta posição ja está ocupada")       
    for p in range(linhas):
        for g in range(colunas):
            print(tabuleiro[p][g], end=" ")
        print()
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
    