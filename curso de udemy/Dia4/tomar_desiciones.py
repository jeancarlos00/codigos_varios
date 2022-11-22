#jemplo
mascota = 'gallina'

if mascota== 'gato':
    print('tienes un gato')
elif mascota=='perro':
    print('tienes un perro')
elif mascota=='conejo':
    print('tienes un conejo')
else:
    print('no se que mascota tienes')

#otro ejemplo

edad = 16
calificacion = 8

if edad>18:
    print('eres mayor de edad')
    if edad<17:
        print('eres menor de edad')
else:
    print('eres menor')

#otro ejemplo

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#otro ejemplo
edad = 16
tiene_licencia = False

if edad >= 18:
    print("Puedes conducir")
elif tiene_licencia==False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")


#######################

habla_ingles = True
sabe_python = False

if  habla_ingles == True and sabe_python == True:
    print ("Cumples con los requisitos para postularte")
elif habla_ingles == True and sabe_python == False:
    print ("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")
