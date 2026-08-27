from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'yellow')

canvas.create_polygon(
    60,50,
    10,100,
    35, 150,
    

    



   

    fill = 'green'
)


canvas.pack()
janela.mainloop()