
def fahrenheit_para_celsius(f):
    """"Converte temperatura de Fahrenheit para Celsius"""
    celsius = (f - 32) * 5 / 9
    return celsius

# a função foi definida, mas nada aconteceu ainda
# precisamos chama-la

temp_f = 98.6
resultado = fahrenheit_para_celsius(temp_f)
print(f"{temp_f}ºF equivalem a {resultado:.2f}ºC")

#tambem podemos chamar diretamente:
print(fahrenheit_para_celsius(32))  #0.0
print(fahrenheit_para_celsius(212))  #  100.0)