#2.	Crear una clase Lamparaque tenga:
#a.	Un método que prenda la lámpara
#b.	Un método que apague la lámpara
#c.	Un método que alterne el prendido y apagado de la lámpara (por ejemplo: si la lámpara estaba prendida,
# al ejecutarse el método pasará a estado apagada)
#d.	Un método que retorne un string según su estado de prendida o apagada:
#i.	Si estaba prendida, el método debe retornar “PRENDIDA”
#ii.	Si estaba apagada, el método debe retornar “APAGADA”
#e.	IMPORTANTE: analizar qué atributo debería tener nuestra clase, para poder implementar las funcionalidades solicitadas.



class Lampara:
    def __init__(self, prendida = True):
        self.prendida = prendida #---------->prendida es el atributo estado

    def get_esta_prendida(self):
        return self.prendida

    def apagar(self):
        if self.prendida:
            self.prendida = False

    def prender(self):
        if not self.prendida:
            self.prendida = True

    def alternar(self):
        self.prendida = not(self.prendida)

    def get_esta_prendida_str(self):
        if self.prendida:
            return("PRENDIDA")
        else:
            return("APAGADA")

lampara=Lampara(True)
print (lampara.get_esta_prendida())
print(lampara.apagar())
print(lampara.prender())
print(lampara.alternar())
print(lampara.get_esta_prendida_str())

