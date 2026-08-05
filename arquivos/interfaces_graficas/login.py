import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("login")
root.geometry("300x400")

label_login = tk.Label(root, text="Faça seu login",font=("arial", 20))
label_login.pack(fill="x" )


frame_imagem = tk.Frame(root,)
meu_frame= tk.Frame(root, bg="blue", width = 150, height=100)
meu_frame.pack(pady=50) 






frame_usuario = tk.Frame(root)
frame_usuario.pack(anchor="w", pady=5)






label_u = tk.Label(frame_usuario, text="Usuário:")
label_u.pack(side="left")





entry_u = tk.Entry(frame_usuario)
entry_u.pack(side="left", padx=4)



frame_senha = tk.Frame(root)
frame_senha.pack(anchor="w", pady=5)

label_s = tk.Label(frame_senha, text="Senha:")
label_s.pack(side="left")

entry_s = tk.Entry(frame_senha, )
entry_s.pack(side="left", padx=5)

  
button = tk.Button( root,
        text = "Entrar",)
button.pack()


frame_checkbox = tk.Checkbutton(root, 
    text="Lembrar-me",
)
frame_checkbox.pack(expand =True, anchor = "w")


label_esqueceu = tk.Label()


root.mainloop()

