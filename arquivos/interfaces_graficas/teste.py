import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Título
label_login = tk.Label(root, text="Faça seu login", font=("Arial", 36, "bold"))
label_login.pack()

# Linha do usuário
frame_usuario = tk.Frame(root)
frame_usuario.pack(anchor="w", pady=10)

label_u = tk.Label(frame_usuario, text="Usuário:")
label_u.pack(side="left")

entry_u = tk.Entry(frame_usuario)
entry_u.pack(side="left", padx=5)


# Linha da senha
frame_senha = tk.Frame(root)
frame_senha.pack(anchor="w", pady=10)

label_s = tk.Label(frame_senha, text="Senha:")
label_s.pack(side="left")

entry_s = tk.Entry(frame_senha, show="*")
entry_s.pack(side="left", padx=5)


# Botão
botao = tk.Button(root, text="Entrar")
botao.pack(anchor="se", pady=10)

root.mainloop()