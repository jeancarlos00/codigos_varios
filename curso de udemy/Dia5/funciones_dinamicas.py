# ejemplo de funciones dinamicas
lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]


def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

#otro ejemplo
lista_numeros = [50,9000]
def suma_menores(lista_numeros):
    suma = 0
    for a in lista_numeros:
        if a in range(1 ,1000):
           suma += a
        else:
            pass
    return suma

#otro ejemplo
lista_numeros = [3,9,69,8,101,6]
def cantidad_pares(lista_numeros):
        par=0
        for a in lista_numeros:
            if a %2==0:
                par += 1
            else:
                 pass
        return par
