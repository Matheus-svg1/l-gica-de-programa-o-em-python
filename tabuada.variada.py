inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

for numero in range(inicio, fim + 1):

    print(f"\n===== TABUADA DO {numero} =====")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")