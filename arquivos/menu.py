def contador_de_filmes():
    contador = 0
    try:
        with open("filmes.txt", encoding = "utf-8") as f:
            for linha in f:
                if linha.strip().startswith("Titulo:"):
                    contador +=1
    except FileNotFoundError:
        print("No arquivo 'filmes.txt' não encontramos informações.")
        return 0
    print(f"Quantidade total de filmes: {contador}")
    return contador


def info_titulo():
    titulo_busca = input("Título: ").strip().lower()
    encontrado = False        
    try:
       with open("filmes.txt", encoding = "utf-8") as f:
        for linha in f:         
            if linha.strip().startswith("Titulo:"):
                titulo = linha.split(":", 1) [1].strip()
                if titulo.lower() == titulo_busca:
                    print(f"Título: {titulo}")
                    try:
                        ano = next(f).strip()
                        diretor =next(f).strip()
                        genero =next(f).strip()
                        duracao =next(f).strip()
                    except StopIteration:
                        print("Sem informações completas para este registro.")
                        return
                    print(ano)
                    print(genero)
                    print(diretor)
                    print(duracao)
                    encontrado = True
                    break

    except FileNotFoundError:
        print("No arquivo 'filmes.txt' não encontramos informações") 
        return
    if not encontrado:
        print("Filme não encontrado")


def filmes_diretores():
  busca_diretor = input("Digite o nome do diretor: ") strip() lower()
def filmes_genero():
    print("lista de generos")

def media_duracao():
    print("tempo de duração")

def sair():
    print("saindo do menu")

def adicionar_filmes():
    print("Adicione seu filme")

def menu():
        print("\nMenu")
        print("0 - Adicionar filme (opcional)")
        print("1 - Quantidade total de filmes")
        print("2 - Informações de um filme pelo título")
        print("3 - Filmes de um diretor específico")
        print("4 - Filmes de um gênero específico")
        print("5 - Média de duração dos filmes")
        print("6 - Sair")

while True:

    menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao =="0":
        print("adicionar_filme()")
    elif opcao == "1":
        contador_de_filmes()
    elif opcao == "2":
        info_titulo()
    elif opcao == "3":
        print("filmes_por_diretor")
    elif opcao == "4":
        print("filmes_por_genero")
    elif opcao == "5":
        print("media_duracao")
    elif opcao == "6":
        print("Saindo do menu")
        break
    else:
        print("Opção inválida. Tente novamente")




    


