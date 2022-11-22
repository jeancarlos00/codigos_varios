from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
from conectar_bd import Comunicacion
from time import strftime


# import pandas as pd


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.actualizar = None
        self.nombre = StringVar()
        self.apellidos = StringVar()
        self.seccion = StringVar()
        self.asistencia = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=5)
        self.base_datos = Comunicacion()

        #self.widgets()

    def widgets(self):
        self.frame_uno = Frame(self.master, bg='white', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='white', height=300, width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0, 1, 2], weight=1)
        self.frame_uno.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Label(self.frame_uno, text='Opciones', bg='white', fg='black',
              font=('Kaufmann BT', 13, 'bold')).grid(colum=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font=('Arial', 9, 'bold'), command=self.actualizar,
               fg='black', bg='deep sky blue', width=20, bd=3).grid(column=2, row=1, pady=5)


a = 1

if a == 1:
    ventana = Tk()
    ventana.title('')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500')
    app = Ventana(ventana)
    app.mainloop()
