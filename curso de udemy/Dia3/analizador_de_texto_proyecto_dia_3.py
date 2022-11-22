print('Analizador de texto!')

#ingresar el texto y tres palaras adicional
texto = input("ingrese el texto o palabra de su elección \n")
palabra1 = input('ingrese la primera palabra \n')
palabra2 = input('ingrese la segunda palabra \n')
palabra3 = input('ingrese la tercera palabra \n')

texto = texto.lower()

print ('\n')
#saber cuantas veces se repite cada palabra en el texto
resultado = (texto.count(palabra1))
resultado1 = (texto.count(palabra2))
resultado2 = (texto.count(palabra3))
print('la letra ' + str(palabra1)+' se repite\n' + " " + str(resultado) + " " + 'veces'.lower())
print('la letra ' + str(palabra2) + ' se repite\n' + " " + str(resultado1) + " "+'veces'.lower())
print('la letra ' + str(palabra3) + ' se repite\n'+ " " + str(resultado2) + " " +'veces'.lower())
print ('\n')

#saber cuantas palabras tiene el texto completo
total = texto.split()
print('el texto tiene un total de:\n' + " " + str(len(total)) + " " + 'palabras')
print ('\n')

#primera palabra
primera_palabra =texto[0]
print('la primera palabra del texto es:\n' + " "+ primera_palabra)
print ('\n')

#ultima palabra
ultima_palabra = texto[-1]
print('la ultima palabra del texto es:\n' + " " + ultima_palabra)
print ('\n')

#invertir el texto
print('si invertimos el texto queda de la siguiente forma:\n' + " " + texto[::-1])
print ('\n')

#saber si la palabra python aparece en el texto

python = ('python' in texto)

if (python==True):
    print('la palabra python si aparece en el texto')
else:
    print('la palabra python no aparece en el texto')