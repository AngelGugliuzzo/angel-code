#1.	Dada una lista de palabras de forma singular, retornar un SET de esas palabras en
# forma plural si aparecen mas de una vez en la lista.

#pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#pluralize(["table", "table", "table"]) ➞ { "tables" }
#pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }


def pluralize(lista):
    contPal = {palabra: lista.count(palabra) for palabra in lista}

    lista2=[]

    for clave, valor in contPal.items():
        if valor > 1:
            clave=clave+"s"
            lista2.append(clave)
        else:
            lista2.append(clave)

    #print(contPal)
    #print(lista2)
    return set(lista2)


#if __name__ == '__main__':
print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))


