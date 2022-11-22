'''def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1,num2,num3]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(1,2,4))'''

#otro ejemplo
def letras_unicas(palabra):
    mi_set = set()

    for letra in palabra:
        mi_set.add((letra))

    mi_lista= list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas('entretenido'))

#otro ejemplo
def ceros_vecinos(*args):
    contador = 0

    for num in args:

        if contador +  1  == len(args):
            return False

        if args[contador] == 0 and args[contador + 1] == 0:

            return True
        else:
            contador += 1

    return False


print(ceros_vecinos(5,6,9,00,8,1,2,2,3,8,7,8,3))

#otro ejemplo

