#a.	Ahora se pide agregar los atributos combustible, distanciaRecorrida y relacionConsumoDistancia
# (por ejemplo: será un número float o decimal, cada 1 litro de combustible recorro 0,5 km)
# y los métodos cargarCombustible y recorrerDistancia.
#b.	El método cargarCombustible sumará más combustible al Vehiculo.
#c.	El método recorrerDistancia verificará si la distancia por parámetro es viable para realizar
# (el trayecto o viaje) y si es así, sumará la distancia recorrida y luego restará el combustible que se gastó
#d.	Para determinar el consumo de combustible se realiza la multiplicación de relacionConsumoDistancia * distancia

from claseVehiculo import Vehiculo
from claseCoche import Coche
from claseCamioneta import Camioneta
from claseBicicleta import Bicicleta
from claseMotocicleta import Motocicleta
from claseMotor import Motor
from claseRendimiento import Rendimiento


print("motor  ")
motor=Motor(120,6,200)
print(motor.cilindrada)
print(motor.velocidad)
print(motor.combustible)
print(" ")

print("vehiculo  ")
vehiculo=Vehiculo("rojo",4)
print(vehiculo.color)
print(vehiculo.ruedas)
print(" ")

print("redimiento   ")
rendimiento=Rendimiento(400,0.5)
print(rendimiento.relacionConsumoDistancia)
print(rendimiento.distanciaRecorrida)
print("   ")

print("coche ")
coche=Coche(vehiculo,motor,rendimiento)
print(coche.cargarCombustible(200,100))
print(coche.recorrerDistancia(50,0.5,200))
print(coche.rendimiento)#------------------->da una direccion de memoria
print(coche.get_ruedas())#------------------>no da nada
print(coche.vehiculo.ruedas)#------------------->poner los atributos por la fuerza, no salen en la lista
print(coche.vehiculo.color)
print(" ")

print("camioneta ")
camioneta=Camioneta(vehiculo,motor,rendimiento,500)
print(camioneta.carga)
print (camioneta.cargarCombustible(100,120))
print(camioneta.recorrerDistancia(30,0.5,125))
#print(camioneta.get_cilindrada())------------------>camioneta no tiene el metodo
print(camioneta.vehiculo.color)#-------------------->si no paso por vehiculo, me da una direccion de memoria
print(camioneta.get_carga())
print(" ")
print(" ")


#para cambiar los datos, tengo que cambiar(instanciar) motor, y rendimiento por vehiculo
print(" ")
print("motocicleta ")
moto=Motocicleta(vehiculo,motor,rendimiento,"zx200")
#print(moto.get_cilindradas())
print(moto.motor.cilindrada)#---------------->lo saco de motor
print(moto.tipo)
print(moto.vehiculo.ruedas)
print(moto.vehiculo.color)

print("   ")
print("   ")
print("bici     ")
bicicleta=Bicicleta("amarillo",2,"mountin")
print(bicicleta.get_tipo())
print(bicicleta.get_color())
print(bicicleta.get_ruedas())
print(bicicleta.color)
print(bicicleta.tipo)