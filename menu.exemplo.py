while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Excluir")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("Cadastrando...")
    elif opcao == "2":
        print("Consultando...")
    elif opcao == "3":
        print("Excluindo...")
    elif opcao == "4":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")