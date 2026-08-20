from jugador import Jugador
from mago import Mago
from guerrero import Guerrero
from objeto import Objeto

#Método principal

def main():
    #crear jugador
    nuevo_jugador = Jugador("Loreto") 

    #crear personajes

    magician = Mago("saruman", 10, 100, 150)
    warrior = Guerrero("Hector el grande", 10, 100, 250)

    #asociar jugador con el pj

    nuevo_jugador.seleccionar_personaje(magician)

    nuevo_jugador.mostrar_personaje()

    #ataque del mago
    magician.atacar()

    #habilidad del mago
    magician.usar_habilidad()

if __name__=="__main__":
    main()

