#7.	Recibiendo una lista de números, escribir una función que retorne una lista sin números
# duplicados y ordenados de menor a mayor.
#●	unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
#●	unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
#●	unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]

def unique_sort(lista):
    sinDuplicados = set(lista)
    Aordenar=[]
    ordenados=[]
    Aordenar=list(sinDuplicados)
    ordenados=sorted(Aordenar)

    return ordenados

print(unique_sort([1, 2, 4, 3]))
print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
print(unique_sort([6, 7, 3, 2, 1]))