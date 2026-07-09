print("digite nome(pressione enter em branco para terminar):")
nomes = []
while True:
    nome = input("Digite o nome: ").strip()
    if nome == "":
        break
    nomes.append(nome)
with open("noems.txt", "w", encoding = "utf-8") as f:
    for n in nomes:
        f.write(n + "\n")




        #with open("nomes.txt", "r", encoding = "utf-8") as f:
        #   conteudo
        