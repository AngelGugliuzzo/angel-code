import random
import CartaClase
import claseMazo
import clasejugador


class Juego:
    def __init__(self):
        self.Jugadores = []
        self.CANTIDAD_DE_JUGADORES = 3


    def añadir_jugador(self, nombre):
        jugador = clasejugador.Jugador(" ")
        jugador.nombre = nombre
            # contacto.apellido =
            # contacto.telefono = telefono
        self.Jugadores.append(jugador)

    def imprimir(self):
        for contacto in self.Jugadores:
            print(contacto.nombre)

    def inicializador_de_cartas(self):  # (i
        contadorDeCartas = 1
      #claseMazo.Mazo.Cartas = []  # ······················> hay que sacarlo, usar el de arriba
        numerosDeCartas = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        palos = ["oro", "basto", "espada", "copas"]
        for numero in numerosDeCartas:
            for tiposDeCartas in palos:
                carta = CartaClase.Carta(0, " ", 0)  # -------->vuelvo a instanciar la clase por cada ciclo
                carta.valor = numero
                carta.palo = tiposDeCartas
                carta.orden = contadorDeCartas
                cartas.append(carta)
                contadorDeCartas = contadorDeCartas + 1

        self.cartas = cartas  # ----------->se lo asigno a la clase para imprimrla
