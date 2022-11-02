class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color



class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad =velocidad
        self.cilindrada = cilindrada

    def get_velocidad(self):
        return (self.velocidad)

    def get_cilindrada(self):
        return (self.cilindrada)


vehiculo=Vehiculo("rojo ",2,)
print(vehiculo.get_color())
print(vehiculo.get_ruedas())
coche=Coche("azul",4,300.00,3.6)
print(coche.color)
print(coche.get_cilindrada())
print(coche.get_velocidad())
print(coche.get_ruedas())
print(coche.get_color())
