with open("exemplo.txt","r") as f:      #readlines() ele lê todo o arquivo e joga para uma lista e depois, precisamos percorrer a lista para buscar o que precisamos, posição [0]
    linhas = f.readlines()               # [0], [1], [2],[3]...
    for linha in linhas: 
        print(linha.strip())