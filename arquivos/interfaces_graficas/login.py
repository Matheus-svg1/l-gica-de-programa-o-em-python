import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("login")
root.geometry("300x300")

label_login = tk.Label(root, text="Faça seu login",font=("arial", 20))
label_login.pack(fill="x" )


minha_imagem = tk.PhotoImage(file="login.png").subsample(3,3)
label_imagem = tk.Label(root, image= minha_imagem )
label_imagem.pack()





frame_usuario = tk.Frame(root)
frame_usuario.pack(anchor="w", pady=5, padx=10)


label_u = tk.Label(frame_usuario, text="Usuário:")
label_u.pack(side="left")


entry_u = tk.Entry(frame_usuario)
entry_u.pack(side="left", padx=20, pady=5)



frame_senha = tk.Frame(root)
frame_senha.pack(anchor="w")

label_s = tk.Label(frame_senha, text="Senha:")
label_s.pack(side="left")

entry_s = tk.Entry(frame_senha, )
entry_s.pack(side="left", padx=28, pady=5)

  
button = tk.Button( root,
        text = "Entrar",)
button.pack()


frame_checkbox = tk.Checkbutton(root, 
    text="Lembrar-me",
)
frame_checkbox.pack(expand =True, side = "left")


frame_esqueceu = tk.Frame(root)
frame_esqueceu.pack(side ="right")

label_esqueceu = tk.Label(frame_esqueceu, text="Esqueci minha senha", fg="blue", cursor="hand2")
label_esqueceu.pack(side="right")


root.mainloop()

