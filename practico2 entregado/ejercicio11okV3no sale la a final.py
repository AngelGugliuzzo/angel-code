#11.	Escribí una función que reciba dos parámetros: un string S y un integer R.
# La función debe devolver un string donde los caracteres consecutivos de S no se repitan
# más que R veces. Tiene que devolver un string con el texto limpio y la cantidad de
# caracteres repetidos correcta.
#Ejemplos:
#●	 "AAA", 2 => "AA"
#●	"AAAAAFFFFOOOA", 2 => "AAFFOOA"
#●	"111223333344", 1 => "1234"
#●	"AABB", 1 => "AB"


def recorte(cadena, num):
    listaDeSalida = []
    conCat = " "
    primero = 0
    cadenaSalida = " "
    largo = len(cadena)-1
    cont = 0
    cont2 = 0
    while cont2 < largo:
        for letra2 in cadena:
            if cont < num:
                listaDeSalida.append(letra2)
                cont = cont + 1
            else:
                if letra2 in listaDeSalida:#------------------->sale, pero de a 2, no hace el OA final
                    #cadena[cont2]==listaDeSalida[cont]:
                   cont2 = cont2 + 1
                else:
                    cont = 0


# primero = cadena.find(letra)
# conCat = cadena[primero:primero + num]

# if conCat not in listaDeSalida:
#   listaDeSalida.append(conCat)

    cadenaSalida = "".join(listaDeSalida)
#    print(cadenaSalida)
    return (cadenaSalida)

print(recorte("AAA",2))
print(recorte("AAAAAFFFFOOOA", 2))
print(recorte("111223333344", 1))
print(recorte("AABB", 1))
