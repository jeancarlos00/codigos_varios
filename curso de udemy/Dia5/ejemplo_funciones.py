tipos_de_cafe = [('expreso',30),('capuchino',45),('normal',15)]

def cafe_mas_caro (lista_cafe):
    precio_mayor = 0
    nombre_mayor = ''
    for nombre,precio in lista_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_mayor = nombre
        else:
            pass

    return (nombre_mayor,precio_mayor)

cafee,precioo= cafe_mas_caro(tipos_de_cafe)
print(f'el cafe mas caro es {cafee} y su precio es {precioo}')
