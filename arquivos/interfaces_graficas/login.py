import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("login")
root.geometry("200x300")

label_login = tk.Label(root, text="Faça seu login")
label_login.pack(fill=tk.X, anchor="w")

#minha_imagem = tk.PhotoImage(file="login.png")

#label_login = tk.Label(root, image=minha_imagem)
#label_login.pack(expand=True)

label_u = tk.Label(root, text="Usuário")
label_u.pack(side="left")






entry_u = tk.Entry()
entry_u.pack(side="left")









root.mainloop()

