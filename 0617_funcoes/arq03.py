def linha():
    """Docstring:Descreve o que a função é"""
    print("+", end="")
    for c in range(2,20):
        print('-', end="")
    print('+')
def coluna():
    """Docstring:Descreve o que a função é:"""
    for l in range(2, 5):
        print('|', end='')
    for c in range(2,20):
        print(' ', end="")
    print('|')
print(linha(), coluna(),linha())

