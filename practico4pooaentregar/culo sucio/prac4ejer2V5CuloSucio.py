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
import CartaClase
import claseMazo
import clasejugador
import ClaseJuego


baraja = claseMazo.Mazo()
jugador=ClaseJuego.Juego()
juego=clasejugador.Jugador("angel")
juego2=clasejugador.Jugador("mateo")
jugador.añadir_jugador("angel")
jugador.añadir_jugador("mateo")
#jugador2.añadir_jugador("mateo")
jugador.imprimir()


# i)
baraja.inicializador_de_cartas()
baraja.imprimir()
# ii)
baraja.mezclar_mazo()
print(" ")
print(" ")
baraja.imprimir()
print(" ")

print(" ")
baraja.sacar_carta()
#baraja.sacar_carta()
#juego.pedir_cartas() #---------->aca salta

print(baraja)
# print(baraja)
print(baraja.cartas_disponibles())
