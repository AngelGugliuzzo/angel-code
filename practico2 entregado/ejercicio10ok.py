#10.	Crear una función que tome un array de numeros y retorne la palabra “Boom!”
# si el dígito 7 aparece en el array. Sino, que retorne “No se encuentra el número 7
# en el array” .
#Ejemplo:
#●	sevenBoom ➞ "Boom!" // El array contiene el número 7
#●	sevenBoom([8, 6, 33, 100]) ➞ “No se encuentra el número 7 en el array” // ninguno de los elementos contiene el número 7
#●	sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!" // 97 contiene el número 7.

def sevenBoom(listaSiete):
    grupoSiete=[7,17,27,37,47,57,67,77,87,97]
    numeroSiete=str(listaSiete)
    corte=False
    cont=0
    tope=len(listaSiete)
    tope2=tope-1

   # while corte != True:
    while cont <= tope2 and corte != True:  # probar or and o <
        if listaSiete[cont] in grupoSiete:
            corte = True
        else:
            cont = cont + 1

    if corte == False:
        return "no se encuentra el 7 en el array"
        #print("no se encuentra el 7 en el array")
    else:
        return "Boom !!!"
        #print("Boom!")




print(sevenBoom([1, 2, 3, 4, 5, 6, 7]))
print(sevenBoom([8, 6, 33, 100]))
print(sevenBoom([2, 55, 60, 97, 86]))