import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("SENAI-Desenvolvimento de Sistemas")
root.geometry("375x200")

#foto
foto= tk.PhotoImage(file="login.png").subsample(3,3)

foto_label= tk.Label(root, image= foto )
foto_label.grid(row=0, column=0, rowspan=5 )

#nome
label_nome=tk.Label(text="Nome:")
label_nome.grid(row=0,column=1, padx=5,pady=5 )

entry_nome=tk.Entry()
entry_nome.grid(row=0,column=2, sticky="ew")

label_genero=tk.Label(text="Gênero:")
label_genero.grid(row=2, column=1)

#genêro
genero = ttk.Combobox(root,values = ["Masculino", "Feminino", "Outro"], state="readonly")
genero.grid(row=2, column=2, sticky="ew")

#cor dos olhos
label_olhos=tk.Label(text="Cor dos olhos:")
label_olhos.grid(row=3, column=1,padx=5,pady=5)


olhos = ttk.Combobox(root,values=["Castanho", "Azul claro","Verde claro"], state="readonly")
olhos.grid(row=3, column=2, sticky="ew")

#altura
label_altura=tk.Label(text ="Altura(cm):")
label_altura.grid(row=4,column=1,padx=5,pady=5)


entry_altura=tk.Entry()
entry_altura.grid(row=4,column=2, sticky="ew")

#peo
label_peso=tk.Label(text="Peso(kg):")
label_peso.grid(row=5,column=1,padx=5,pady=5)


entry_peso=tk.Entry()
entry_peso.grid(row=5,column=2, sticky="ew")

#botão
def botao_command():
        messagebox.showinfo(
    "Resultado",
    f"Seu nome é {entry_nome.get()}")

button=tk.Button(text="Enviar", command=botao_command)
button.grid(row=6,column=2,sticky="e")



root.mainloop()  




