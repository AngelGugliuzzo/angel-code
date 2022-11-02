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
    listaAux=[]
    listaRecortada=[]
    conCat = " "
    primero = 0
    cadenaSalida = " "
    largo = len(cadena)-1
    cont = 0
    cont2 = 0
    cont4=0
    for letra in cadena:
        listaAux.append(letra)
    print(listaAux,"lista auxiliar1")

    listaDeSalida1 = list(reversed(listaAux))
    print(listaDeSalida1, "reversa")

    while cont4<=largo-1:
         if listaAux[cont4]== cadena[cont4+1]:
             listaRecortada.append(listaDeSalida1[cont4])
             cont4=cont4+1
         else:
             listaRecortada.append(listaDeSalida1[cont4])
            # listaRecortada.append(" ")
             cont4=cont4+1
    cont4=cont4+1

    #print(listaRecortada,"lista recortada")






    while cont2 < largo:
        for letra2 in cadena:
            if cont < num:
                listaDeSalida1.append(letra2)
                cont = cont + 1
            else:
                if letra2 in listaDeSalida1:#------------------->sale, pero de a 2, no hace el OA fina
                #if cadena[cont2]==listaDeSalida[cont]:
                   cont2 = cont2 + 1
                else:
                    cont = 0


# primero = cadena.find(letra)
# conCat = cadena[primero:primero + num]

# if conCat not in listaDeSalida:
#   listaDeSalida.append(conCat)

    cadenaSalida = "".join(listaDeSalida1)
#    print(cadenaSalida)
    return (cadenaSalida)

print(recorte("AAA",2))
print(recorte("AAAAAFFFFOOOA", 2))
print(recorte("111223333344", 1))
print(recorte("AABB", 1))
