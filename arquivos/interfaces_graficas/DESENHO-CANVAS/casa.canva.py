from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x600")
canvas = Canvas(janela, width = 400, height= 300, bg= 'white')

canvas.create_rectangle(      #PAREDE
    30,300,700,100,
    fill='gray',
)


canvas.create_rectangle(       #PORTA
    175, 200, 250, 400,
    fill = 'brown',
)



canvas.create_rectangle(        #JANELA
    80, 250, 160,180,
    fill = 'light gray' ,

)


canvas.create_rectangle(       #JANELA
    
    350,180, 270, 250,
    fill = 'light gray' ,

)


canvas.create_polygon(          #TELHADO
    200, 0, 
    405, 100,
    30, 100,
    fill = 'black'
)



canvas.create_oval(240, 255, 250, 265, fill = 'black' )    #maçaneta



canvas.create_line(

    100, 100, 150, 250,
    fill = 'black',
    width=3)

canvas.pack()

janela.mainloop()