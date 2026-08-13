from tkinter import *
from tkinter import ttk

#cores-----------------------------
cor0 =  "#FFFFFF"  #white / branca
cor1 =  "#333333"  #black / preto
cor2 =  "#fcc058"  #orange / laranja
cor3 =  "#fff873"  #yellow / amarelo
cor4 =  "#34eb3d"  #green / verde
cor5 =  "#e85151"  #red / vermelho
fundo = "#3b3b3b"  #


janela = Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo=Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#CONFIGURANDO OS JOGADORES
#jogador pessoa
app_pessoa = Label(frame_cima, text="Jogador", height=1, anchor="center",
                   bg =cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)


#barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)


#pontuação
app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)


#separação da pontuação
app_vs = Label(frame_cima, text=":", height=1, anchor="center",
               bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)





#jogador PC
app_PC = Label(frame_cima, text="PC", height=1, anchor="center",
                   bg =cor1, fg=cor0, font=("Ivy 10 bold"))
app_PC.place(x=220, y=70)


#barra marcou pontos
app_PC_linha = Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_PC_linha.place(x=255, y=0)


#pontuação
app_PC_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_PC_pontos.place(x=195, y=19)


#barra de empate
app_empate = Label(frame_cima, text="", width=255, anchor="center", bg=cor3,
                   fg=cor0, font=("Ivy 1 bold"))
app_empate.place(x=0, y=95)



janela.mainloop()
