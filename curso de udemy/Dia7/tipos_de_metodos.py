# metodos de instancias(los normales)
'''
1-acceden y modifican los atributos del objeto
2-acceden a otros metodos
3-modifican el estado de la clase
ejemplo de metodos de instancias:
'''
class Pc:

    def __init__(self, mouse, teclado):
        self.mouse = mouse
        self.teclado = teclado

    def color_de_la_pc(self, color):
        print(f'El color de la pc es: {color}\nLa pc trae incluido un {self.mouse} y un {self.teclado}')


venta = Pc('mouse', 'teclado')
venta.color_de_la_pc('negro')


# metosos de clases
'''
1-no acceden a los atributos de instancias 
2-si acceden a los atributos de clases y los modifican
3-para acceder a estos metodos de clases se hace de la sgt manera:
'''


class Carro:
    @classmethod
    def carroceria(cls, color):
        print(f'la carroceria es de color {color}')


civic = Carro()
civic.carroceria('blanco')


#metodos estaticos
'''
1-no acceden a los atributos de instancias 
2-tampoco acceden a los atributos de clases ni los modifican
3-para acceder a estos metodos de clases se hace de la sgt manera:
'''


class Motocicleta:

    @staticmethod
    def moto():
        print(f'la moto es un 115')


jaja = Motocicleta()
jaja.moto()



