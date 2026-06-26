#exercicio: calcular a média
#crie um função chamada calcular_média que receba uma lista de numeros inteiros e retorne a média aritmética desses valores
#Entrada  uma lista de interos ex: [7,8,9,10]
# processo -  somar todos os valores e dividir pela quantidade de elementos
#saída - retornar o resultado como números float.
def calcular_media():
    """"Calcular a média aritmética"""
    notas = [5, 8, 2, 12]
    somar_notas = sum(notas)
    media = somar_notas//len(notas)
    return media
print(calcular_media())




def calcular_media(numeros):
    """ recebe uma lista de inteiros e retona a média aritmética.
    
    parametros:
    - numeros: lista de inteiros
    Retorna:
    - fooat: media artitmética ( 0.0 se a lista for vazia)"""

    if not numeros:
        return ).0
    total = sum(numeros)
    retun float(total) /len numeros

