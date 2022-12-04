from tkinter import * 


root = Tk()
root.geometry("800x500")
root.resizable(False, False)
root.title("Registro de Estudiantes")
root.config(bg="light blue")

def agregar():
    cajon.insert(END, caja_nombre.get(),caja_apellido.get(),caja_curso.get(),caja_numero.get(),caja_nota1.get(),caja_nota2.get(),caja_nota3.get(),caja_nota4.get())
    
'''
def eliminar():
    cajon.delete()'''



#label de datos
label_nombre = Label(root, text="Nombre",bg="light blue")
label_nombre.place(x=50, y=70)

label_apellido = Label(root, text="Apellido", bg="light blue")
label_apellido.place(x=50, y=110)

label_curso = Label(root, text="Curso", bg="light blue")
label_curso.place(x=50, y=150)

label_numero = Label(root, text="Numero", bg="light blue")
label_numero.place(x=50, y=190)

label_nota1 = Label(root, text="Nota 1", bg="light blue")
label_nota1.place(x=250, y=70)

label_nota2 = Label(root, text="Nota 2", bg="light blue")
label_nota2.place(x=250, y=110)

label_nota3 = Label(root, text="Nota 3", bg="light blue")
label_nota3.place(x=250, y=150)

label_nota4 = Label(root, text="Nota 4", bg="light blue")
label_nota4.place(x=250, y=190)

#cajas de entrada
caja_nombre = Entry(root)
caja_nombre.place(x=50, y=90)


caja_apellido = Entry(root)
caja_apellido.place(x=50, y=130)

caja_curso = Entry(root)
caja_curso.place(x=50, y=170)

caja_numero = Entry(root)
caja_numero.place(x=50, y=210)

caja_nota1 = Entry(root)
caja_nota1.place(x=250, y=90)

caja_nota2 = Entry(root)
caja_nota2.place(x=250, y=130)

caja_nota3 = Entry(root)
caja_nota3.place(x=250, y=170)

caja_nota4 = Entry(root)
caja_nota4.place(x=250, y=210)

cajon = Listbox(root, width=95, height=10)
cajon.place(x=120, y=300)

#crear menu
menu_central = Menu(root) 
root.config(menu=menu_central)
archivos_menu = Menu(menu_central, tearoff=0)


archivos_menu.add_command(label="Nuevo")
archivos_menu.add_command(label="Abrir")
archivos_menu.add_command(label="Guardar Como")
archivos_menu.add_separator()
archivos_menu.add_command(label="Salir")
menu_central.add_cascade(label="Archivo", menu=archivos_menu)

#Botones
btn1 = Button(root, text="Agregar", bg="white", height=1, width=9, command=agregar)
btn1.place(x=500, y=90)

btn2 = Button(root, text="Eliminar", bg="white", height=1, width=9)
btn2.place(x=500, y=150)

btn3 = Button(root, text="Modificar", bg="white", height=1, width=9)
btn3.place(x=500, y=210)








root.mainloop()