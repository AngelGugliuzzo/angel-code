#6.	Crear una función que eleve al cuadrado cada dígito del número pasado por parámetro.
#●	square_digits(9119) ➞ 811181
#●	square_digits(2483) ➞ 416649
#●	square_digits(3212) ➞ 9414

def square_digits(numero):
    lista1=[]
    lista2=[]
    cadena=" "
    salida=0
    lista1 = list(map(int, str(numero)))

    for numero in lista1:
        lista2.append(numero**2)

    for numero2 in lista2:
        cadena=cadena+str(numero2)

    salida=int(cadena)

    #return(cadena)#----------->lo puedo devolver como cadena o como integer
    return (salida)

print(square_digits(9119))
print(square_digits(2483))
print(square_digits(3212))