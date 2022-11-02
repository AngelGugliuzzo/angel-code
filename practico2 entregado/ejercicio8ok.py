#8.	Crear una función que tome dos listas y retorne True, si la segunda lista continua el orden de la primer lista y
#False de lo contrario. Determina si la segunda lista es la primer lista “movida” en una posición hacia la derecha.
#●	simon_says([1, 2], [5, 1]) ➞ True
#●	simon_says([1, 2], [5, 5]) ➞ False
#●	simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
#●	simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False

def simon_says(lista1,lista2):

    listaDeNumeros=[0,1,2,3,4,5,6,7,8,9]
    listaDeComparacion=[]
    largoLista2=0
    largoLista2=len(lista2)
    ultimoLista2=lista2[largoLista2-1]

    for indice in range(1,largoLista2):
        listaDeComparacion.append(lista2[indice])

    for numero in listaDeNumeros:
        if ultimoLista2==numero:
           listaDeComparacion.append((listaDeNumeros[listaDeNumeros.index(numero)+1]))

    return lista1[0]==listaDeComparacion[0]



print(simon_says([1, 2], [5, 1]))
print(simon_says([1, 2], [5, 5]))
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))

