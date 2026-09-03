import tkinter as tk
from tkinter import ttk
root=tk.Tk()
def escalas(ohms):
    #Menor ou igual a 999
    if ohms <= 999:
        return f"{ohms} Homns",
    #Maior que 999 homs e menor ou igual a 99.999 (99999)
    elif 999 < ohms <=99999:
        kilo_ohms = ohms / 1000
        return f"{kilo_ohms}Kilohoms (kΩ)"
    #Valores acima de 99.999
    else:
        mega_homs = 100000
        return f"{mega_homs}Megahoms(MΩ)"


# Exemplos de teste:
print(escalas(150))    # Saída: 150 Ohms
print(escalas(4700))   # Saída: 4.7 Kiloohms (kΩ)
print(escalas(100000)) # Saída: 0.1 Megaohms (MΩ)

root.mainloop()