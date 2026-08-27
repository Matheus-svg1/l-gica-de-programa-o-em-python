valores = []
while True:
    try:
        valor = int(input("Digite um valor (0 para encerrar):").strip())
    except Exception:
        print("Entrada inválida.Digite um número inteiro.")
        continue

    if valor == 0:
        break
    valores.append(valor)

if not valores:
    print("Nenhum valor foi encontrado.")

n = len(valores)
if n % 2 == 1:
    mid = n // 2
    print(f"Valore central:{valores[mid]}")
else:
    a = valores[n//2-1]
    b = valores[n // 2]
    print(f"Lista com comprimento par. Valores centrais: {a} e {b} ")

