#los diccionarios se escriben entre llaves y primero se escribe la clave y luego el valor
diccionario = {'c1':'valor1','c2':'valor2'}

print(diccionario)

#podemos guardar en una variable para luego imprimir de un codigo en especifico

resultado = diccionario['c2']
print(resultado)

#un diccionario puede contener diferentes tipos de datos y listas y diccionarios dentro de diccionarios

#a los diccionarios se le pueden agregar mas elementos y sustituir de la misma manera
#ejemplo
diccionario['c3']='valor3'
print(diccionario)

#para imprimir las claves de el diccionario se realiza con el sgt metodo keys

print(diccionario.keys())

#para imprimir los valores que tiene el diccionario se realiza con el sgt metodo values

print(diccionario.values())

#para conocer todo lo que hay dentro del diccionario lo hacemos con el metodo items

print(diccionario.items())












#mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict[('puntos')]["points2"][1])