import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def escalas(ohms):
<<<<<<< HEAD

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
=======
    #Menor ou igual a 999
    if ohms <= 999:
        return f"{ohms} Ω",
    #Maior que 999 homs e menor ou igual a 99.999 (99999)
    elif 999 < ohms <=99999:
        kilo_ohms = ohms / 1000
        return f"{kilo_ohms:.1f}(kΩ)"
    #Valores acima de 99.999
    else:
        mega_homs = ohms / 10000
        return f"{mega_homs}(MΩ)"
>>>>>>> 160456b3558408719f85d78cbb4ed4774888cd45


# Exemplos de teste:
print(escalas(150))
print(escalas(4700))
print(escalas(100000))

root.mainloop()