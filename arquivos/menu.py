def menu():
    print("\nMenu")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

opcao = input("Escolha uma opção: ").strip()

if opcao =="0":
    print("adicionar_filme()")
elif opcao == "1":
    print("Contar_filmes")
elif opcao == "2":
    print("info_por_titulo")
elif opcao == "3":
    print("filmes_por_diretor")
elif opcao == "4":
    print("filmes_por_genero")
elif opcao == "5":
    print("media_duracao")