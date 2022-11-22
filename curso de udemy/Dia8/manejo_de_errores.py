def suma():
    n1 = int(input('numero1: '))
    n2 = int(input('numero2: '))
    print(f'resultado: {n1 + n2}')
    print('Gracias por sumar con nosotros')



try:
    suma()
except TypeError:
    print('estas intentando concatenar distintos tipos de datos')
except ValueError:
    print('no es un numero')
else:
    print('hiciste todo bien')
finally:
    print('eso fue todo')



#otro ejemplo
def pedir_numero():

    while True:
        try:
            numero = int(input('escribe un numero: '))
        except:
            print('ese no es un numero')
        else:
            print(f'acabas de ingresar el numero: {numero}')
            break
    print('Gracias')

pedir_numero()







#nota: para conocer los tipos de errores podemos entrar a la documentacion de python y buscar (excepciones incorporadas)
#teoria de la prueba de error
'''try:
    #codigo que queremos probar
except:
    #codigo a ejecutar si no hay un error
else:
    #codigo a ejecutar si no hay un error
finally:
    #codigo que se va a ejecutar de todos modos'''


def yanco(num1, num2):

    try:
        print(num1 + num2)
    finally:
        print(num1 + num2)

        
yanco()