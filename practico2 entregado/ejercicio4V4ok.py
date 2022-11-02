#4.	Crear una función que tome dos listas y determine si existe lo que en poker se denomina
 #   “color” (cinco cartas del mismo palo). La primer lista son las 5 cartas repartidas en la mesa.
 #   La segunda lista representa 2 cartas en tu mano.
 #   Notación: número y palo de la carta (S = Espadas, H = Corazones, D = Diamantes, C = Picas)
#    separados por un guion bajo.
#●	check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamantes
#●	check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // espadas
#●	check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False

def check_flush(cartas1, cartas2):
    mazo=[]
    contadores=[0,0,0,0]
    contS=0
    contH=0
    contD=0
    contC=0
    cont=0
    cont2=0


    lista1L = str(cartas1)
    lista1=lista1L.split("_")
    lista1L=list(lista1)

    lista2L=str(cartas2)      #para el split deben ser caracteres
    lista2=lista2L.split("_")
    lista2L = list(lista2)


    for palo in lista2L:               #es lo mismo que asignarlo directamente
        lista1L.append(palo)

    mazo = str(lista1L)
   # print(mazo)                       #desactivado para pruebas unitarias

    for baraja in mazo:
        if baraja == "S":
            contS = contS + 1
            contadores[0] = contS
        if baraja == "H":
            contH = contH + 1
            contadores[1] = contH
        if baraja == "D":
            contD = contD + 1
            contadores[2] = contD
        if baraja == "C":
            contC = contC + 1
            contadores[3] = contC

    if max(contadores) >= 5:
        return True
    else:
        return False


print(check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]))
print(check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]))
print(check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]))
