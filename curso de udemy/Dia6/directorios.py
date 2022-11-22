#a la ruta se le debe colocar siempre la doble barra invertida \\ para que funcione

#con el metodo getcwd(),puedes ver la ruta actual
import os

ruta = os.getcwd()

print(ruta)

#con el metodo chdir podemos acceder a otra ruta o directorio

ubicacion = os.chdir('C:\\Users\\Jean Carlos\\Desktop\\eliminar')

yanco = open('programando.txt')
angel = yanco.read()
print(angel)

#con el metodo makedirs se crea un nuevo directorio o una carpeta

ubicacion = os.makedirs('C:\\Users\\Jean Carlos\\Desktop\\eliminar\\borrar')


#con el metod path.basename()  podemos recibir el nombre de la base

ruta ='C:\\Users\\Jean Carlos\\Desktop\\eliminar'

elemento = os.path.basename(ruta)

print(elemento)


#con el metodo path.dirname podemos recibir el nombre de la ruta

ruta ='C:\\Users\\Jean Carlos\\Desktop\\eliminar'

elemento = os.path.dirname(ruta)

print(elemento)

#con el metodo path.split podemos obtener en una tupla el nombre de la ruta mas el nombre de la base

ruta ='C:\\Users\\Jean Carlos\\Desktop\\eliminar'

elemento = os.path.split(ruta)

print(elemento)

#con el metodo rmdir podemos eliminar carpetas

os.rmdir('C:\\Users\\Jean Carlos\\Desktop\\eliminar\\borrar')


#el modulo path lo utilizaremos de la siguiente forma para acceder a una ruta tanto desde mac como windows
#primero importamos de la libreria pathlib el objeto Path
#en este caso no se usa la barra invertida sino normal