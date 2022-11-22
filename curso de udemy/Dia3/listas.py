#las listas pueden tener diferentes tipos de datos, se pueden modificar a diferencia de los string y van entre corchetes
mi_lista=['a','b','c','d']
print(mi_lista)

#en las listas podemos saber cuantos elementos tiene la variable con el metodo len
yanco = ['arroz','habichuela','carne','ensalada']

print(len(yanco))

#tambien podemos usar indices con las listas
hello = ['a','c','b']
print(hello[0])

#las listas tambien se pueden concatenar
primera = ['yo quiero ']
segunda = ['aprender a programar']
tercera = primera+segunda
print(tercera)

#las listas si pueden ser modificadas a diferncia de los string normales
comida = ['locrio con habichuela']
comida[0]='moro'
print(comida)

#en la listas podemos agregar utilizando append
desayuno = ['platano','yuca']
desayuno.append('huevo')
print(desayuno)

#utlizando pop se pude eliminar variables
nombre = ['rosa','jimenez']
nombre.pop(1)
print(nombre)

#las listas se pueden ordenar utilizando sort
jaja = ['a','s','h','w','b']
jaja.sort()
print(jaja)

#las listas se pueden ordenar de atras para alante usando reverse
siii = ['a','b','c','d','e']
siii.reverse()
print(siii)