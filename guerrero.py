from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre, nivel, vida, fuerza):
        super().__init__(nombre, nivel, vida)
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} atacó"
              f" con {self.poder_magico} de poder de fueza")

    def usar_habilidad(self):
        print(f"{self.nombre} coraza de aliento")