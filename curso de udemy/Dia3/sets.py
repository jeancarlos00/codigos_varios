#los sets son como los string que no se pueden modificar ni agregar, ni pueden tener diccionarios ni listas pero si tuple

mi_set = set((1,2,3))

print(type(mi_set))

print(mi_set)

#ejemplo de una consulta

print(2 in mi_set)

#para unir los set lo hacemos de la sgt manera con el metodo union()

c1 = set((1,2,3))
c2 = set((4,5,6))
c3 = c1.union(c2)
print(c3)

#para agregar valores a los set lo hacemos con el metodo .add

c1.add(7)

print(c1)

#para eliminar valoes de los set lo hacemos con el metodo remove()

c1.remove(3)

print(c1)

#para limpiar el set usamos el metodo clear()

c1.clear()
print(c1)

#el metodo pop se usa para eliminar al azar cualquier elemento del set