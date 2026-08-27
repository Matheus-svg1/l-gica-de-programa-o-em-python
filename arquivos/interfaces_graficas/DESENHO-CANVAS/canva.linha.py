from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'white')

canvas.create_line(

    10, 10, 200, 180,
    fill = 'black',
    width=3)

canvas.create_line(

    10, 10, 10, 250,
    fill = 'black',
    width=3)

canvas.create_line(

    10, 10, 250, 10,
    fill = 'black',
    width=3)

canvas.pack()
janela.mainloop()