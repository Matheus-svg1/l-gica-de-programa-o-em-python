
linhas = 3
colunas = 3
jogador_atual = "Jogador 1"
simbolo = "X"
tabuleiro = []
jogadas = 0

for p in range(linhas):
    linha = []
    for g in range(colunas):
        linha.append(" ")
    tabuleiro.append(linha)
print(f"Vez do {jogador_atual} ({simbolo})")
while True:
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 9)
        print()

    coluna_escolhida = int(input("Escolha uma coluna de (0 a 2): "))
    linha_escolhida = int(input("Escolha uma linha de (0 a 2): "))
    
    #função para verificar vitória

    if linha_escolhida < 0 or linha_escolhida > 2 or coluna_escolhida < 0 or coluna_escolhida >2:
        print("Posição inválida!")
        continue

    if  tabuleiro[linha_escolhida][coluna_escolhida] == " ":
        tabuleiro[linha_escolhida][coluna_escolhida] = simbolo
        jogadas += 1
    else:
        print("Esta posição ja está ocupada")       
    for p in range(linhas):

    #LINHAS
        for i in range(3):
            if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2]== simbolo:
                print(f"O jogador {jogador_atual} venceu!")
                exit()
    #COLUNAS
    for i in range(3):
        if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
            print(f"O jogador {jogador_atual} venceu!")
            exit()
     #DIAGONAL PRINCIPAL   
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        print(f"O jogador {jogador_atual} venceu!")  
        exit()
    #DIAGONAL SECUNDÁRIA    
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        print(f"O jogador {jogador_atual} venceu!")
        exit()
     #EMPATE   
    if jogadas == 9:
        print("Empate!")
        exit() 
    #TROCA DE JOGADOR
    if jogador_atual == "Jogador 1":
        jogador_atual = "Jogador 2"
        simbolo = "O"
    else:
        jogador_atual = "Jogador 1"
        simbolo = "X"

                