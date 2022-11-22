#los index sirven para saber en que posicion del codigo binario se encuentra una palabra

palabra = 'jean carlos'
solucion = palabra[3]
print(solucion)

# tambien se puede encontrar palabras dentro de un texto

frase = 'la teoria es importante pero la practica es mejor'

print(frase.index('mejor'))

# el metodo rindex se usa para encontrar de atras para lante

dicho = 'solo hay que practicar y ya'
print(dicho.rindex('s'))

