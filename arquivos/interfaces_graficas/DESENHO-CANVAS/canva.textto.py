from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x350")
canvas = Canvas(janela, width = 400, height= 300, bg= 'black')
canvas.create_text(200,100, text="Poligono", font=('Arial',12, 'bold'), fill="red")

canvas.create_text(200,150, text="sexta-feira, terça-feira", font=('Arial',12), fill="white", anchor = "w")

canvas.create_text(200,200, text="quarta-feira, quinta-feira", font=('Arial',12), fill="orange", anchor = "e")
canvas.pack()

janela.mainloop()