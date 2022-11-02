class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def get_ruedas(self):
        return self.ruedas

    def get_color(self):
        return self.color



class Coche(Vehiculo):
    def __init__(self, color,ruedas,velocidad,cilindrada):#--------------->no puedo pasarlos color y ruedas
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
coche=Coche(300,6)#--------------------------get color y rueda da cilindros y velocidad
print(coche.get_cilindrada())#------------------>me pasa cilindros y velocdad, no pasa color y ruedas
print(coche.get_velocidad())
print(coche.get_ruedas())
print(coche.get_color())
