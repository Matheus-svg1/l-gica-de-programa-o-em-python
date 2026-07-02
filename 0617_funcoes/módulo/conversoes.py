# conversoes.py
def celsius_fahrenheit(C: float) -> float:
    """converte tempertura em celsius para farhrenheit.

    Formula: f = C * 9 / 5 + 32
    """
    return C * 9 / 5 + 32 


def metros_quilometros(m: float) -> float:
    """ Converte distancia em metros para quilometros.
    1km = 1000 m"""
    return m / 1000
