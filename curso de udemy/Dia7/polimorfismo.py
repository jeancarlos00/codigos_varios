


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero1 = Arquero()
mago1 = Mago()
samurai1 = Samurai()





personajes1 = arquero1.atacar()
personajes2 = mago1.atacar()
personajes3 = samurai1.atacar()