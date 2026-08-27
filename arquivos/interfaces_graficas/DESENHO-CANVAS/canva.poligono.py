from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'white')

canvas.create_polygon(
    100, 50, 
    150, 150,
    50, 150,
    fill = 'green'
)


canvas.pack()
janela.mainloop()