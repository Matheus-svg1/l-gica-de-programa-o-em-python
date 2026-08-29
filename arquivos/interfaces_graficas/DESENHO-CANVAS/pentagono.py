from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'yellow')


canvas.create_polygon(
    10,100,
    60,50,
    110,100,
    85,150,
    35,150,
    
    

    



   

    fill = 'green'
)


canvas.pack()
janela.mainloop()