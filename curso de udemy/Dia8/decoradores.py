def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula_decorada('el YAnco')



'''
#asi se usa sin los decoradores
def cambiar_letra(tipo):

    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas

operacion = cambiar_letra('may')

operacion('tengo hambre')
'''