#3.	Crear una función que permita realizar una operación aritmética que incluya adición, sustracción, multiplicación y división teniendo como parámetro de la función los siguientes ejemplos: “12 + 24” , “23 - 21”, “12 // 12”, “12 * 21”
#En el caso de la división por cero, retornar -1 o algún mensaje que diga que no se puede realizar la operación.

#operacion_aritmetica("12 + 12") ➞ 24 // 12 + 12 = 24
#operacion_aritmetica("12 - 12") ➞ 24 // 12 - 12 = 0
#operacion_aritmetica("12 * 12") ➞ 144 // 12 * 12 = 144
#operacion_aritmetica("12 // 0") ➞ -1 // 12 / 0 = -1


def operacion_aritmetica(operacion):

    if "+" in operacion:
        operadores=operacion.split("+")
        return int(operadores[0])+int(operadores[1])
    if "-" in operacion:
        operadores = operacion.split("-")
        return int(operadores[0]) - int(operadores[1])
    if "*" in operacion:
        operadores = operacion.split("*")
        return int(operadores[0]) * int(operadores[1])
    if "//" in operacion:
        operadores = operacion.split("//")
        if int(operadores[1])==0:
            return -1
        else:
            return int(operadores[0]) // int(operadores[1])


if __name__ == '__main__':
    print(operacion_aritmetica("12 + 12"))
    print(operacion_aritmetica("12 - 12"))
    print(operacion_aritmetica("12 * 12"))
    print(operacion_aritmetica("12 // 0"))






