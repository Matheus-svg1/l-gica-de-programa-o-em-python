senha = input("Digite uma senha")

has_upper = False
has_lower = False
has_digit = False
has_especial = False

for ch in senha:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch.isespecial():
        has_especial = True

erros = []
if len(senha)<8:
    erros.append("Mínimo 8 caracteres.")
if not has_upper:













































