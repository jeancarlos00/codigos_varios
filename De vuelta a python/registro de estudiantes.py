from tkinter import *
import pandas as pd
from pandastable import Table
from PIL import Image, ImageTk
import sqlite3

#crear ventana
ventana = Tk()
ventana.title('Registro de estudiantes')
ventana.geometry('800x500')
ventana.config()
ventana.resizable(False, False)

#conexion a la base de datos
conexion = sqlite3.connect("base_de_datos")
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DATOS(id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, numero TEXT, seccion TEXT, sexo TEXT, grado TEXT, correo TEXT, materia TEXT)''')


#agregar datos a la base de datos mediante textobox
def insertar_datos():
    nombre = caja_nombre.get()
    apellido = caja_apellido.get()
    numero = caja_numero.get()
    seccion = caja_seccion.get()
    sexo = caja_sexo.get()
    grado = caja_grado.get()
    correo = caja_correo.get()
    materia = caja_materia.get()
    conexion = sqlite3.connect("base_de_datos")
    cursor = conexion.cursor()
    consulta = "INSERT INTO DATOS(nombre, apellido, numero, seccion, sexo, grado, correo, materia) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(consulta, (nombre, apellido, numero, seccion, sexo, grado, correo, materia))
    conexion.commit()


#cargar imagen
imagen = Image.open("C:/Users/Jean Carlos/Desktop/Proyectos de python/De vuelta a python/fondo.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = Label(ventana, image = imagen_tk, width=ventana.winfo_screenwidth(),height=ventana.winfo_screenheight())
label_imagen.pack()

#Labels
label_central = Label(ventana, bg="light blue", text="Datos del estudiante", font="bold")
label_central.place(x=340, y=30)

label_nombre = Label(ventana, bg="light blue", text="Nombre:", font="bold")
label_nombre.place(x=150, y=80)

label_apellido = Label(ventana, bg="light blue", text="Apellidos:", font="bold")
label_apellido.place(x=150, y=120)

label_numero = Label(ventana, bg="light blue", text="Numero de orden:", font="bold")
label_numero.place(x=150, y=160)

label_seccion = Label(ventana, bg="light blue", text="Sección:", font="bold")
label_seccion.place(x=150, y=200)

label_sexo = Label(ventana, bg="light blue", text="Sexo:", font="bold")
label_sexo.place(x=465, y=80)

label_grado = Label(ventana, bg="light blue", text="Grado:", font="bold")
label_grado.place(x=465, y=120)

label_correo = Label(ventana, bg="light blue", text="Correo:", font="bold")
label_correo.place(x=465, y=160)

label_materia = Label(ventana, bg="light blue", text="Materia:", font="bold")
label_materia.place(x=465, y=200)


#Caja de texto
caja_nombre = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_nombre.place(x=290, y=80, )



caja_apellido = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_apellido.place(x=290, y=120)

caja_numero = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_numero.place(x=290, y=160)

caja_seccion = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_seccion.place(x=290, y=200)

caja_sexo = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_sexo.place(x=550, y=80)

caja_grado = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_grado.place(x=550, y=120)

caja_correo = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_correo.place(x=550, y=160)

caja_materia = Entry(ventana, width=25, highlightbackground="red", highlightcolor="red", highlightthickness=2)
caja_materia.place(x=550, y=200)

caja_grande = Listbox(ventana, width=85, height=8, highlightbackground="black", highlightcolor="black", highlightthickness=2)
caja_grande.place(x=120, y=350)


#Botones de la aplicacion
btn_agregar = Button(ventana, width=20, text="Agregar", highlightbackground="black", highlightcolor="black", highlightthickness=5, command=insertar_datos)
btn_agregar.place(x=50, y=300)




btn_modificar = Button(ventana, width=20, text="Modificar", highlightbackground="black", highlightcolor="black", highlightthickness=5)
btn_modificar.place(x=300, y=300)

btn_eliminar = Button(ventana, width=20, text="Eliminar", highlightbackground="black", highlightcolor="black", highlightthickness=5)
btn_eliminar.place(x=550, y=300)

#Menu de la aplicacion
menu_central = Menu(ventana)

ventana.config(menu=menu_central)
archivos_menu = Menu(menu_central, tearoff=0)
importar_menu = Menu(menu_central,tearoff=0)

archivos_menu.add_command(label="Importar excel")
archivos_menu.add_command(label="Imprimir")
archivos_menu.add_command(label="Guardar Como")
archivos_menu.add_separator()
archivos_menu.add_command(label="Salir")
menu_central.add_cascade(label="Archivo", menu=archivos_menu)







conexion.close()



ventana.mainloop()

