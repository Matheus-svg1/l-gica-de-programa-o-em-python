try:
    n = int(input("Digite um número: ").strip())

except Exception:
    print("Entrada inválida.")

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
    
