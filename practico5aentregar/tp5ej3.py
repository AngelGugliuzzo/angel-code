#a.	Ahora se pide agregar los atributos combustible, distanciaRecorrida y relacionConsumoDistancia
# (por ejemplo: será un número float o decimal, cada 1 litro de combustible recorro 0,5 km)
# y los métodos cargarCombustible y recorrerDistancia.
#b.	El método cargarCombustible sumará más combustible al Vehiculo.
#c.	El método recorrerDistancia verificará si la distancia por parámetro es viable para realizar
# (el trayecto o viaje) y si es así, sumará la distancia recorrida y luego restará el combustible que se gastó
#d.	Para determinar el consumo de combustible se realiza la multiplicación de relacionConsumoDistancia * distancia


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color

#------------------------------------------------------------------------------------------


class Coche(Vehiculo):
    def __init__(self, color,ruedas,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.combustible = combustible
        self.distaciaRecorrida = distaciaRecorrida
        self.relacionConsumoDistancia=relacionConsumoDistancia

    def get_velocidad(self):
        return (self.velocidad)

    def get_cilindrada(self):
        return (self.cilindrada)

    def cargarCombustible(self,combustible,tanqueAnterior):
         self.combustible=combustible+tanqueAnterior   #----------------->como acumulo, contra que sumo
         return self.combustible #solo para poder verlo en pantalla

    def recorrerDistancia(self,distanciaRecorrida,relacionConsumoDistancia,distancia):
         trayecto=relacionConsumoDistancia*distancia
         if trayecto > (distanciaRecorrida*relacionConsumoDistancia):
             return self.combustible-((distanciaRecorrida+trayecto)*relacionConsumoDistancia)



         # ej:200 km * relacionConsumoDistancia
         # ej:200km *  0,5 l/km=100 km
#-------------------------------------------------------------------------------------
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga,combustible,distaciaRecorrida,relacionConsumoDistancia):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia)
        self.carga = carga

    def get_carga(self):
        return self.carga


#------------------------------------------------------------------------------------------------
class Bicicleta(Vehiculo):   #preguntar por la bicicleta a motor, en tal caso, la ubiccion esta bien parametros
    def __init__(self,color,ruedas,tipo):  # cil y vel 0
            Vehiculo.__init__(self, color,ruedas)
            self.tipo=tipo

    def get_tipo(self):
        return self.tipo

#---------------------------------------------------------------------------------------------------

class Motocicleta(Coche):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada,combustible,distaciaRecorrida,relacionConsumoDistancia):
            Coche.__init__(self, color,ruedas,tipo,velocidad,cilindrada,distaciaRecorrida,relacionConsumoDistancia)
            self.tipo=tipo
           # self.velocidad = velocidad
           # self.cilindrada=cilindrada

    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.cilindrada


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
print(moto.tipo)
print(moto.get_ruedas())
#hacer clase coche motor, poner las clases en arcivo
print("     ")
bicicleta=Bicicleta("amarillo",2,"mountin")
print(bicicleta.get_tipo())
print(bicicleta.get_color())
print(bicicleta.get_ruedas())
print(bicicleta.color)
print(bicicleta.tipo)