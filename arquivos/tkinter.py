import tkinter as tk
# cria a janela principal
root = tk.Tk()
#Cria um rótulo (label) com o texto "hello, world!"
message = tk.Label(root, text = "Hello, World!")

#posiciona o rótulo na janela 
message.pack()

#Define o tamanho da janela (largura x altura + posição + posição y)
root.geometry("400x200+50+250")

#inicia o loop principal da interface grafica
root.mainloop()