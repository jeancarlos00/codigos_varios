def cantidad_atributos (**kwargs):

    return len(kwargs)

#otro ejemplo
def lista_atributos(**kwargs):
    lista = []
    for calor in kwargs.values():
        lista.append(calor)
    return lista

#otro ejemplo
def describir_persona(nombre, **kwargs):
    print(f'características de {nombre}:')
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


nombre = 'María'
kwargs = {'color_ojos': 'azules', 'color_pelo': 'rubio'}


print(describir_persona(nombre, **kwargs))