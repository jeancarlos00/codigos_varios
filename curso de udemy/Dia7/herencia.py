

class Padre:
    def comida(self):
        print('la comida estaba perdida')


class Madre:
    def trabajo(self):
        print('el trabajo esta bueno')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


yanco = Nieto()
yanco.trabajo()

print(Nieto.__bases__)



####################################
class Vertebrado():
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass