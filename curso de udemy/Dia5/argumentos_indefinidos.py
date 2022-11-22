'''def suma_cuadrados(*args):
    resultado = 0
    for args in args:
        resultado += args **2
    return resultado


print(suma_cuadrados(32, 2, 5))'''


#otro ejemplo

def suma_cuadrados(*args):
    resultado = 0
    for args in args:
        resultado += abs(args)
    return resultado


print(suma_cuadrados(-32, 2, 5))

#otro ejemplo

'''

def numeros_persona(nombre, *args):
    contador = 0
    for args in args:
        contador += args
    return nombre, 'la suma de tus números es' + str(args)


print(numeros_persona('jjj',5+5))'''

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

