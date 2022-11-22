def crear_lista():
    lista = []
    for n in range(1, 10):
        lista.append(n)

    return lista


print(crear_lista())

#otro ejemplo:
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()
