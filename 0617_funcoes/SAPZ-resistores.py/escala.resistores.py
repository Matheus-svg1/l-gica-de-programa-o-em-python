import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def escalas(ohms):

    # Maior que 999 e menor ou igual a 99.999
    if 999 < ohms <= 99999:
        kilo_ohms = ohms / 1000
        return f"{kilo_ohms} Kilohms (kΩ)"

    # Valores acima de 99.999
    elif ohms > 99999:
        mega_ohms = ohms / 1000000
        return f"{mega_ohms} Megohms (MΩ)"

    # Menor ou igual a 999
    else:
        return f"{ohms} Ohms"


# Exemplos de teste:
print(escalas(150))
print(escalas(4700))
print(escalas(100000))

root.mainloop()