class Carro:
    placa = True  #atributos de clase
    def __init__(self,color,marca):
        self.color = color
        self.marca = marca


mi_carro = Carro('rojo','hyundai')


print(f'El color del vehiculo que tengo es  {mi_carro.color}, y la marca es {mi_carro.marca}')
print(Carro.placa)