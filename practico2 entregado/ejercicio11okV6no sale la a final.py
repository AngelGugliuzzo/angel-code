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
    listaDeSalida  = []
    listaDeSalida1 = []
    listaDeSalida2 = []
    listaAux=[]
    cadenaSalida = " "
    largo = len(cadena)-1
    cont =0
    cont2 = 0
    cont4=0




    for letra in cadena:
        listaAux.append(letra)
    print(listaAux,"lista auxiliar1")

    listaDeSalida1 = list(reversed(listaAux))
    print(listaDeSalida1, "reversa")

    while cont<=largo:
        for letra2 in listaDeSalida1:
            if cont2 <= num  :
                listaDeSalida.append(letra2)
                cont2 = cont2 + 1
            #else:
             #   cont=largo
    cont=cont+1


   # for letra3 in listaDeSalida1: #contar los numeros de lista salida
   #     if cont2<num:
   #        listaDeSalida2.append(letra3)
   #        cont2=cont2+1
    #    else:
    #        cont2=1




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
