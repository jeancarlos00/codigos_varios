from tkinter import *

# iniciar tkinter
app = Tk()

# tamaño de la ventana
app.geometry('1030x600+150+50')

# evitar maximizar
app.resizable(0, 0)

# titulo de la ventana
app.title('Sistema Escolar')

# color de fondo de la ventana
app.config(bg='burlywood')

# panel superior
panel_superior = Frame(app, bd=2, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema escolar', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(app, bd=2, relief=FLAT)
panel_izquierdo.pack(side=LEFT)



















# evitar que la pantalla se cierre
app.mainloop()