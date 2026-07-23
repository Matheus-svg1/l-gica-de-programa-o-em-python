def filmes_por_diretor():
    diretor_busca = input("Titulo: ").strip().lower()
    encontrado = False        
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





























def genero():
    diretor_busca = input("Digite o nome do diretor").strip().lower()
    encontrado = False
    try:
        with open("filmes.txt", encoding="utf-8") as f:

            while True:
                try:
                    titulo = next(f).strip()
                    ano = next(f).strip()
                    diretor = next(f).strip()
                    genero = next(f).strip()
                    duracao = next(f).strip()
                except StopIteration:
                    break

                busca = diretor.split(":",1)[1].strip().lower()

                if busca in diretor_busca:
                    print(titulo)
                    encontrado = True

        if not encontrado:
            print("Nenhum filme encontrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")