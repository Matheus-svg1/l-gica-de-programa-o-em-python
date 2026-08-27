lista = []
for i in range(3):
    nome = input("Digite seu nome: ")
    lista.append(nome)
with open("nomes1.txt", "w") as f:
    for nome in lista:
        f.write(nome + "\n")

