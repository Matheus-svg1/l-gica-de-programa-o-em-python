import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("login")
root.geometry("200x300")

label_login = tk.Label(root, text="Faça seu login").pack(fill="x")

#minha_imagem = tk.PhotoImage(file="login.png")

#label_login = tk.Label(root, image=minha_imagem)
#label_login.pack(expand=True)

label_u = tk.Label(root, text="Usuário").pack(side="left")






entry_u = tk.Entry().pack(side="left")









root.mainloop()

