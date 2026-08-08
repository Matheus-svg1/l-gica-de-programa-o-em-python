import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.title("SENAI-Desenvolvimnento de Sistemas")
root.geometry("300x300+50+100")

def mostrar_selecao(event):
    selecao = cidades.curselection()
    messagebox.showinfo("Seleção", cidades.get(selecao))

tk.Label(root, text="Qual cidade você gostaria de conhecer ?").place(x=50,y=20)

cidades = tk.Listbox(root, selectmode=tk.BROWSE, width=24)
cidades.place(x=40,y=65)

for cidade in ["Brasília", "Florianópolis", "Porto Alegre", "Rio de janeiro", "são paulo"]:
    cidades.insert(tk.END, cidade)

cidades.bind("<<ListBoxSelectd>>", mostrar_selecao)

botao = tk.Button(root, text = "Sair", command=quit)
botao.place(x=125,y=250)

root.mainloop()
