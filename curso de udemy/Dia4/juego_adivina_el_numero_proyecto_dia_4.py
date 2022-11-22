import random
contador = 0
aleatorio = random.randint(1,101)


print('Bienvenido al juego de yensel')


nombre = input('cual es tu nombre?\n')
print(f'Hola  "{nombre}"  el juego consiste en adivinar el numero del 1 al 100.\n\nTienes 8 intentos restantes:')


while contador < 8:
    numero = int(input('ingrese el numero:\n'))
    contador += 1

    if numero == aleatorio:
        print(f'Felicidades {nombre}, has acertado el numero correcto')
        break

    if numero < 1 or numero > 100:
        print('favor introduce un numero valido,del 1 al 100:\n')


    if numero < aleatorio:
        print('tu numero fue menor al mio:')

    if numero > aleatorio:
        print('tu numero fue mayor al mio')
else:
    print(f'Lo siento por ti pero has perdido, el numero era el:\n{aleatorio}')






