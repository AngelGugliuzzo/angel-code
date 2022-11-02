#1.	Crear una clase Instrumento que:
#a.	Tenga como atributos el precio (int), marca(string) y modelo(string).
#b.	El método tocar().
#c.	Luego se crearán las clases Guitarra, Batería y Piano, las cuales heredarán de la clase Instrumento.
#d.	Es importante que cada instrumento, al llamarse al método tocar() tenga su PROPIA IMPLEMENTACIÓN, es decir:
#si creo un objeto de la clase Guitarra y llamo al método tocar(), en la consola de salida voy a visualizar el mensaje
# “Sonando como una guitarra”, y así por cada objeto de su respectiva clase

class Instrumento:
    def __init__(self, precio, marca, modelo):
        self.precio = precio
        self.marca = marca
        self.modelo = modelo

    def tocar(self):
        return("paso")


class Guitarra(Instrumento):
    def __init__(self, precio, marca, modelo):
        Instrumento.__init__(self, precio, marca, modelo)#---------------->esto reemplaza al super


    def tocar(self):
        return ("tocando guitarra ")


class Bateria(Instrumento):
    def __init__(self, precio, marca, modelo):
        Instrumento.__init__(self, precio, marca, modelo)


    def tocar(self):
        return ("tocando bateria")


class Piano(Instrumento):
    def __init__(self, precio, marca, modelo):
        Instrumento.__init__(self, precio, marca, modelo)
        #super().__init__(precio, marca, modelo)#--------------------->no hace falta

    def tocar(self):
        return ("tocando el piano")


instrumento = Instrumento(10, "yamaja", "x200")
print(instrumento.tocar())
guitarra=Guitarra(20000,"fender","x22")
print(guitarra.tocar(),guitarra.marca)
bateria=Bateria(1000,"zidigian","f3000")
print(bateria.tocar(),bateria.marca)
piano=Piano(1000000,"steinhauser","l22")
print(piano.tocar(),piano.marca)
print(piano.precio)

