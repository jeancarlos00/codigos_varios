'''Python. Al escribir código, es de uso permanentemente para
solucionar dudas relacionadas al funcionamiento de métodos y
los argumentos que reciben.
Python
TOTAL
Si utilizas PyCharm:
Sostén el cursor sobre el
nombre del método del
que deseas obtener
información. Se
desplegará una ventana
flotante.
https://docs.python.org/es/3.9/library/index.html
También, debes mantener cerca la documentación oficial de
Python (o Biblioteca Estándar de Python), que contiene toda la
información necesaria:
No dejes de buscar en Google tus dudas, para hallar una
explicación que se ajuste a ti.'''

#ejemplo usando el metodo (lsptrip) que aprendi usando la documentacion
a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

b=a.lstrip(',:_#,,,,,,:::____##')

print(b)

#otro ejemplo que aprendi a usar el metodo (insert) usando la documentacion
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

#otro ejemplo que aprendi
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)