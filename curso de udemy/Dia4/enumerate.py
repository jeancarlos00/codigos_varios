#ejemplo sin enumerate
abecedario = ['a','b','c','d','e']
aprendiendo = 0

for jean in abecedario:
        print(aprendiendo,jean)
        aprendiendo += 1

#ejemplo con enumerate
abanico = ('a','b','c')

for corriente in enumerate (abanico):
    print(corriente)

#otro ejemplo con enumerate
comida = ('arroz','abuchuela','carne')

for comida,postre in enumerate (comida):
    print(comida,postre)

#otro ejemplo
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#otro ejemplo
lista_indices = list (enumerate("Python"))
print (lista_indices)
#otro mas
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for a , b in enumerate(lista_nombres):
    if 'M' in (b):
        print(a)