import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("login")
root.geometry("200x300")

label_login = tk.Label(root, text="Faça seu login")
label_login.pack(fill=tk.X, anchor="w")


frame_imagem = tk.Frame(root,)
meu_frame= tk.Frame(root, bg="lightgray", width = 400, height=300)
meu_frame.pack(pady=50) 


frame_imagem = tk.PhotoImage(file="login.png")
imagem_original = Image.open("login.png")

label = tk.Label(root, image=frame_imagem)


label.pack(expand=True)


label_login = tk.Label(root, image= frame_imagem)
label_login.pack(expand=True,)




frame_usuario = tk.Frame(root)
frame_usuario.pack(anchor="w", pady=5)






label_u = tk.Label(frame_usuario, text="Usuário:")
label_u.pack(side="left")





entry_u = tk.Entry(frame_usuario)
entry_u.pack(side="left", padx=5)



frame_senha = tk.Frame(root)
frame_senha.pack(anchor="w", pady=5)

label_s = tk.Label(frame_senha, text="Senha:")
label_s.pack(side="left")

entry_s = tk.Entry(frame_senha, show="*")
entry_s.pack(side="left", padx=5)

  
button = tk.Button( root,
        text = "Entrar",)



frame_checkbox = tk.Checkbutton(root, 
    text="Esqueci minha senha",
)
frame_checkbox.pack(expand =True, side = "right")




button.pack()
root.mainloop()

