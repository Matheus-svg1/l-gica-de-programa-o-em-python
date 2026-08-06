import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("SENAI-Desenvolvimento de Sistemas")
root.geometry("200x500")


foto= tk.PhotoImage(file="login.png").subsample(4,4)

foto_label= tk.Label(root, image= foto )
foto_label.grid(row=0, column=0, rowspan=5 )


label_nome=tk.Label(text="Nome:")
label_nome.grid(row=0,column=1)


entry_nome=tk.Entry()
entry_nome.grid(row=0,column=2)

label_genero=tk.Label(text="Gênero:")
genero = ttk.Combobox(root,)
label_genero.grid(row=1, column=1)

values = ["Primeiro", "Segundo", "Terceiro"]

root.mainloop()  




