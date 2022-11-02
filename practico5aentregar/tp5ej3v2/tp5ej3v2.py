#a.	Ahora se pide agregar los atributos combustible, distanciaRecorrida y relacionConsumoDistancia
# (por ejemplo: será un número float o decimal, cada 1 litro de combustible recorro 0,5 km)
# y los métodos cargarCombustible y recorrerDistancia.
#b.	El método cargarCombustible sumará más combustible al Vehiculo.
#c.	El método recorrerDistancia verificará si la distancia por parámetro es viable para realizar
# (el trayecto o viaje) y si es así, sumará la distancia recorrida y luego restará el combustible que se gastó
#d.	Para determinar el consumo de combustible se realiza la multiplicación de relacionConsumoDistancia * distancia

from tp5ej3claseVehiculo import Vehiculo
from tp5ej3claseCoche import Coche
from tp5ej3camioneta import Camioneta
from tp5ej3Bicicleta import Bicicleta
from tp5ej3motocicleta import Motocicleta

coche=Coche("rojo",4,100,6,200,300,0.5)

print(coche.cargarCombustible(200,100))
print(coche.recorrerDistancia(50,0.5,200))
camioneta=Camioneta("rojo",4,120,6,30,50,100,0.5)

print(" ")
print(camioneta)#---------------------------------------->direccion de memoria
print(camioneta.carga)
print (camioneta.cargarCombustible(100,120))
print(camioneta.recorrerDistancia(30,0.5,125))
print(camioneta.get_cilindrada())

print(" ")
moto=Motocicleta("azul",2,"zx2",200,1100,10,400,0.5)
print(moto.get_cilindrada())
print(moto.get_ruedas())
print(moto.velocidad)
print(moto.tipo)

print("  ")
bicicleta=Bicicleta("amarillo",2,"mounting")
print(bicicleta.get_tipo())
print(bicicleta.get_color())
print(bicicleta.get_ruedas())
print(bicicleta.color)
print(bicicleta.tipo)