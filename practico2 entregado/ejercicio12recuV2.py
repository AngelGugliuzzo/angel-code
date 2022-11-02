#12. Escribir una función recursiva que reciba un conjunto de caracteres únicos,
# y un número 𝑘, e imprima todas las posibles cadenas de longitud 𝑘 formadas con los
# caracteres dados(permitiendo caracteres repetidos). Ejemplo:
#●    combinaciones(['a', 'b', 'c'], 2) debe imprimir
#aa ab ac ba bb bc ca cb cc

def combinaciones(lista,num):
    listaDeSalida = []
    cadenaSalida=[]

    if num >= 0:
        for cont2 in range(0,len(lista)):
            listaDeSalida.append( lista[num] + lista[cont2])
        listaDeSalida = listaDeSalida + combinaciones(lista, num - 1)

    #cadenaSalida=sorted(listaDeSalida)
    #cadenaSalida = "".join(listaDeSalida)

    return(sorted(listaDeSalida))
    #return("".join(cadenaSalida))



print(combinaciones(['a', 'b', 'c'], 2))


