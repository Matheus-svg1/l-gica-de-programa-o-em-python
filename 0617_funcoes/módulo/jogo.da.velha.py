
linhas = 3
colunas = 3
jogador= "X"
tabuleiro = []
jogadas = 0

for p in range(linhas):
    linha = []
    for g in range(colunas):
        linha.append(" ")
    tabuleiro.append(linha)

while True:
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
    if i < 2:
        print("---------")
    coluna_escolhida = int(input("Escolha uma coluna de (0 a 2): "))
    linha_escolhida = int(input("Escolha uma linha de (0 a 2): "))

    if linha_escolhida < 0 or linha_escolhida > 2 or coluna_escolhida < 0 or coluna_escolhida >2:
        print("Posição inválida!")
        continue

    if  tabuleiro[linha_escolhida][coluna_escolhida] == " ":
        tabuleiro[linha_escolhida][coluna_escolhida] = jogador
        jogadas += 1
    else:
        print("Esta posição ja está ocupada")       
    for p in range(linhas):
    
        for g in range(colunas):
            print(tabuleiro[p][g], end=" ")
        print()

    #LINHAS
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2]== jogador:
            print(f"O jogador {jogador} venceu!")
            exit()
    #COLUNAS
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            print(f"O jogador {jogador} venceu!")
            exit()
     #DIAGONAL PRINCIPAL   
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            print(f"O jogador {jogador} venceu!")  
            exit()
    #DIAGONAL SECUNDÁRIA    
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            print(f"O jogador {jogador} venceu!")
            exit()
     #EMPATE   
    if jogadas == 9:
        print("Empate!")
        exit() 
    #TROCA DE JOGADOR
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

                