#5.	Un número es “Disarium” si la suma de los dígitos elevados a su respectiva posición
# da como resultado el mismo número en sí mismo. Crear una función que determine si un
# número es o no “Disarium”.
#●	is_disarium(75) ➞ False # 7^1 + 5^2 = 7 + 25 = 32
#●	is_disarium(135) ➞ True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
#●	is_disarium(544) ➞ False
#●	is_disarium(518) ➞ True
#●	is_disarium(466) ➞ False
#●	is_disarium(8) ➞ True

#isDisarium 135 = 1¹ + 3² + 5³ = 1 + 9 + 125 = 135
#Test driven development
#135
#"135" -> 1-0 3-1 5-2 // 1-1 3-2 5-3
# Implementar

def is_disarium(numero):
    numero = str(numero)
    acumulador = 0
    for caracter in numero:
        posicion = numero.index(caracter) + 1
        acumulador += int(caracter) ** posicion
    return numero == str(acumulador)


print(is_disarium(75))  #➞ False # 7^1 + 5^2 = 7 + 25 = 32
print(is_disarium(135)) #➞ True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
print(is_disarium(544)) #➞ False
print(is_disarium(518)) #➞ True
print(is_disarium(466)) #➞ False
print(is_disarium(8))   #➞ True