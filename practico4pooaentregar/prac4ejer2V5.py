#2. 	Se solicita crear una implementación de una baraja española, para ello se solicita:
#a. 	Crear una clase Carta que posea los atributos de valor y palo.
#       ACLARACION: solamente los valores entre el 1 y el 12 (8 y 9 no se incluyen)
#b. 	Crear una clase Baraja que:
#i.	    Contenga un conjunto de cartas iniciales (40 por defecto).
#       Se recomienda tener algún inicializador de cartas, es decir que entregue todas las cartas correspondientes
#ii.	La acción de barajar: cambia de posición todas las cartas aleatoriamente
#iii.	La acción de pedir la siguiente carta que está en la baraja, cuando no haya más o se haya
#       llegado al final, se indica al usuario que no hay más cartas.
#iv.	Devolver la cantidad de cartas disponibles que aún se  puede repartir
#v.	    La acción de poder dar cartas: dado un número de cartas que nos pidan,
#       le devolveremos ese número de cartas. En caso de que haya menos cartas que las pedidas,
#       no devolveremos nada pero debemos indicárselo al usuario.
#vi.	ACLARACION: tratar a la baraja como si fuese una pila, es decir extraer las cartas desde un solo “lado”

import random
import CartaClase                                          #(a


class Baraja:  # (b
    def __init__(self):  # ----------------->no se muy bien si pasar la clase
        self.cartas = []  # ------> hacer metodo que cargue las cartas, dos for anidados

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
        paloUltima = ultimaCarta.palo
        return "valor : {}, palo : {}".format(valorUltima, paloUltima)

 #iii) y iv)
    def sacar_cartas_del_mazo(self):
        contadorDeCartas = 0
        MAZO = 40
        pedidoDeCarta = str(input("precione Q para pedir una carta, o X para salir "))
        while pedidoDeCarta == "q":
            print(baraja)
            contadorDeCartas +=  1
            if contadorDeCartas == 40:
                print("sin cartas en el mazo")
                pedidoDeCarta = "x"
            else:
                print("Quedan : ", 40 - contadorDeCartas, " cartas en el mazo")
                pedidoDeCarta = str(input("precione Q para pedir una carta, o X para salir "))

    #v)

    def pedir_cartas(self):
        contadorDeCartas=0
        cartasAPedir=int(input("cuantas cartas desea : "))
        cantidadEnMazo=len(baraja.cartas)
        while contadorDeCartas<=cartasAPedir or cartasAPedir>=cantidadEnMazo:
        #contadorDeCartas += 1
             print(baraja)
             contadorDeCartas += 1
        if cartasAPedir>=cantidadEnMazo:
            print("no me alcanzan las cartas")



baraja = Baraja()
#i)
baraja.inicializador_de_cartas()
baraja.imprimir()
#ii)
baraja.mezclar_mazo()
print(" ")
print(" ")
baraja.imprimir()
print(" ")

#iii) y iv)
#baraja.sacar_cartas_del_mazo()
#v)
baraja.pedir_cartas()
print(" ")
baraja.sacar_carta()
baraja.sacar_carta()
#print(baraja.sacar_carta())

#print(baraja)------------>saco las cartas de a uno
print(baraja)
#print(baraja)
print(baraja.cartas_disponibles())



