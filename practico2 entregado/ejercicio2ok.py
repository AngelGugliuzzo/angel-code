#2.	Escribir una función que retorne True si cada secuencia consecutiva de unos
#es seguida por una secuencia consecutiva de ceros de la misma longitud

#same_length("110011100010") ➞ True
#same_length("101010110") ➞ False
#same_length("111100001100") ➞ True
#same_length("111") ➞ False

def same_length(lista):
    sumaCeros = 0
    sumaUnos = 0
    bandera = True

    palabraBinaria=list(lista)

    largo=len(palabraBinaria)

   # print(largo)
    #print(palabraBinaria)


    for unosYceros in palabraBinaria:
        if unosYceros=="1":
            sumaUnos=sumaUnos+1
        else:
            if unosYceros=="0":
                sumaCeros=sumaCeros+1

    return sumaCeros==sumaUnos

print(same_length("110011100010"))
print(same_length("101010110"))
print(same_length("111100001100"))
print(same_length("111"))

#print(same_length("10101"))
#print(same_length("11001100")) #si pongo los ceros y unos, lo ve como entero
#print(same_length("111100001000"))
#print(same_length("111001"))



#12
#['1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0']
#True
#9
#['1', '0', '1', '0', '1', '0', '1', '1', '0']
#False
#12
#['1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0']
#True
#3
#['1', '1', '1']
#False


#5
#['1', '0', '1', '0', '1']
#False
#8
#['1', '1', '0', '0', '1', '1', '0', '0']
#True
#12
#['1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0']
#False
#6
#['1', '1', '1', '0', '0', '1']
#False
