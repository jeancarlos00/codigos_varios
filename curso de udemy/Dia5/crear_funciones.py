def saludar (nombre):
    '''
    por lo regular cuando se crean funciones se le coloca un comentario para saber de que trata esta funcion.

    '''

    print('Hola ' +nombre)

saludar('jean')


#otro ejemplo
nombre_persona='Lucas'
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")


#otro ejemplo
un_numero= 5
def cuadrado(un_numero):
    print(un_numero**2)

#otro ejemplo
def potencia(numero1, numero2):
    return numero1**numero2
print(potencia(3,4))

#otro ejemplo
palabra = "Curso de Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra