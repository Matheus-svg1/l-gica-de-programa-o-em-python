from tkinter import *
from tkinter import ttk
#baixar o PIL usando; pip install Pillow
from PIL import Image, ImageTk
import random




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

global escolha_pessoa
global escolha_pc
global pontos_pessoa
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc=0
rodadas =5

#jogada lógica
def jogar(jogada):
    global pontos_pessoa
    global pontos_pc
    global rodadas

    opcoes =["pedra", "papel", "tesoura"]


    if rodadas >0:
        print(rodadas)
        escolha_pc = random.choice(opcoes)
        escolha_pessoa = jogada
        print(escolha_pessoa, escolha_pc)

    else:
        terminar_jogo()


#função iniciar jogo
def iniciar_jogo():
    global icone_pedra
    global icone_papel
    global icone_tesoura

    global btn_pedra
    global btn_papel
    global btn_tesoura


    # configurando o frame a abaixo
    icone_pedra = Image.open("./imagens/pedra.png")
    icone_pedra = icone_pedra.resize((50,50),
                                 Image.Resampling.LANCZOS)

    icone_pedra = Image.Photoimage(icone_pedra)
    btn_pedra = Button(frame_baixo, width=50, height=50,
                   image=icone_pedra, bg=cor0, fg=cor0,
                   compound="center", font=("Ivy 10 bold"),
                   anchor = "center", relief="flat", command=lambda: jogar("pedra"))
    btn_pedra.place(x=15, y=60)




    icone_papel = Image.open("./imagens/papel.png")
    icone_papel = icone_papel.resize((50,50), Image.Resampling.LANCZOS)

    icone_papel = Image.Photoimage(icone_papel)
    btn_papel = Button(frame_baixo, width=50, height=50,
                   image=icone_papel, bg=cor0, fg=cor0,
                   compound="center", font=("Ivy 10 bold"),
                   anchor = "center", relief="flat", command=lambda: jogar("papel"))
    btn_papel.place(x=95, y=60)

    

    icone_tesoura = Image.open("./imagens/tesoura.png")
    icone_tesoura = icone_tesoura.resize((50,50),
                                 Image.Resampling.LANCZOS)

    icone_tesoura = Image.Photoimage(icone_tesoura)
    btn_tesoura = Button(frame_baixo, width=50, height=50,
                   image=icone_tesoura, bg=cor0, fg=cor0,
                   compound="center", font=("Ivy 10 bold"),
                   anchor = "center", relief="flat", command=lambda: jogar("tesoura"))
    btn_tesoura.place(x=170, y=60)




#
    



janela.mainloop()
