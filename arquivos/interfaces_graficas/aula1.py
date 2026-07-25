import tkinter as tk
# cria a janela principal
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

root.title("Começando a desenvolver...")
#Ler o título da janela
title = root.title()

title2 = root.title()
#Cria um rótulo (label) com o texto "hello, world!"
message = tk.Label(root, text = title)

message2 = tk.Label(root, text = title2 )
#posiciona o rótulo na janela 
message.pack()

#Define o tamanho da janela (largura x altura + posição + posição y)
root.geometry("600x100+50+250")

#inicia o loop principal da interface grafica
root.mainloop()