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
    titulo_busca = input("Titulo: ").strip().lower()
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
    diretor_busca = input("Titulo: ").strip().lower()
    contador = 0    
    try:
       with open("filmes.txt", encoding = "utf-8") as f:
        ultimo_titulo = ""
        for linha in f: 
            s = linha.strip()        
            if linha.strip().startswith("Titulo:"):
               ultimo_titulo = linha.split(":", 1) [1].strip()
            elif s.startswith("Diretor:"):
                diretor = linha.split(":", 1) [1].strip()
                if diretor.lower() == diretor_busca:
                    contador += 1
                    print(f"-: {ultimo_titulo}")

    except FileNotFoundError:
        print("No arquivo 'filmes.txt' não encontramos informações") 
        return
    print(f"Total de filmes do diretor '{diretor_busca}': {contador}")
    return contador

        


def filmes_genero():
    genero_busca = input("Titulo: ").strip().lower()
    contador = 0     
    try:
        with open("filmes.txt", encoding = "utf-8") as f:
            ultimo_titulo = ""
            for linha in f: 
                s = linha.strip()        
                if linha.strip().startswith("Titulo:"):
                   ultimo_titulo = linha.split(":", 1) [1].strip()
                elif s.startswith("Diretor:"):
                    genero = linha.split(":", 1) [1].strip()
                    if genero.lower() == genero_busca:
                        contador += 1
                        print(f"-: {ultimo_titulo} ({genero})")
    
    except FileNotFoundError:
            print("No arquivo 'filmes.txt' não encontramos informações") 
            return
    print(f"Total de filmes do diretor '{genero_busca}': {contador}")
    return contador
    


def media_duracao():
    soma = 0
    cont = 0 
    try:
        with open("filmes.txt", encoding = "utf-8") as f:
            for linha in f:
                s = linha.strip()
                if s.startswith("Duração:"):
                    try:
                        minutos = int(s.split(":", 1)[1].srip().split()[0])
                    except (ValueError, IndexError):
                        continue
                    soma += minutos
                    cont +=1
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    if cont == 0:
        print("Nenhuma duração válida encontrada")
    else:
        media = soma / cont
        print(f"Média de duração:{media:.2f} minutos")
        return media

def sair():
    print("saindo do menu")

def adicionar_filmes():

    titulo = input("digite um nome de filme: ").strip()
    ano = int(input("Digite o ano do filme: ")).strip()
    diretor = input("Digite o nome do diretor").strip()
    genero = input("Digite o genero do filme").strip()
    Duração = input("Digite a duração do filme").strip()

    with open("filmes.txt", "a"), "encoding=utf-8" as f:
        f.write("\n")
        f.write(F"titulo: {titulo}\n")
        f.write(f"ano: {ano}\n")

        f.writ(f"diretor")



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
        adicionar_filmes()
    elif opcao == "1":
        contador_de_filmes()
    elif opcao == "2":
        info_titulo()
    elif opcao == "3":
        filmes_diretores()
    elif opcao == "4":
        filmes_genero()
    elif opcao == "5":
        media_duracao()
    elif opcao == "6":
        print("Saindo do menu")
        break
    else:
        print("Opção inválida. Tente novamente")
