import random
import CartaClase
#import claseMazo
import clasejugador

class Mazo:  # (b
    def __init__(self):  # ----------------->no se muy bien si pasar la clase
        self.cartas = []

    def inicializador_de_cartas(self):  # (i
        contadorDeCartas = 1
        cartas = []  # ······················> hay que sacarlo, usar el de arriba
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

    def imprimir(self):
        for carta in self.cartas:
            print(carta.orden, carta.palo, carta.valor)

    def mezclar_mazo(self):  # (ii
        random.shuffle(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) > 0:
            print("No está vacía")
            return self.cartas.pop()
        # return False
        else:
            print("Está vacía")
        #   return True

    def cartas_disponibles(self):
        return len(self.cartas)

    # este __str__ imprime de a uno
    def __str__(self):
        ultimaCarta = CartaClase.Carta  # --------------->declare la ultimaCarta de clase carta, para extraer los atributos
        ultimaCarta = self.cartas.pop()
        valorUltima = ultimaCarta.valor  # ---------->arme dos variables para poder extraer los atributos para concatenar
        paloUltima =  ultimaCarta.palo
        return "valor : {}, palo : {}".format(valorUltima, paloUltima)

