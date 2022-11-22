class Ole:
    def __init__(self, precios, ofertas, carritos):
        self.precios = precios
        self.ofertas = ofertas
        self.carritos = carritos

    def __str__(self):
        return (f'En ole tenemos los {self.precios} con mayor {self.ofertas} y {self.carritos} disponibles')


super_mercado = Ole('precios desde 1 peso en adelante', 'ofertas desde 50%', 'mas de 1000 carritos')
print(str(super_mercado))


##########################################################################################################################

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas


biblioteca = Libro('jaja','jbb','lkj')
print(len(biblioteca.cantidad_paginas))

###########################################################################################################################

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
