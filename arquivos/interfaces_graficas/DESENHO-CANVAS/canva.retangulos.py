from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'yellow')

canvas.create_rectangle(
    50, 50, 150, 100,
    fill = 'green',
    outline= 'orange'
)


#canvas.create_rectangle(
#    x1, y1, x2, y2,
#    fill = 'green',
#    outline= 'red')


#(x1, y1) = canto superior esquerdo
#(x2, y2) = canto inferiro esquerdo
canvas.pack()
janela.mainloop()