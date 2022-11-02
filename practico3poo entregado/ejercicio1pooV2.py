#1.	Crear una clase Rectángulo que tenga
#a.	Los atributos base y altura.
#b.	Crear el constructor de la clase que reciba por argumento los valores de la base y la altura.
#c.	Los métodos necesarios para:
#i.	Calcular el área. La fórmula es base*altura
#ii.	El perímetro. La formula es 2*base + 2*altura

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #def superficie(self):
    def get_area(self):
        return (str(self.base * self.altura))

    def get_perimetro(self):
        #return (str(2 * self.base + 2 * self.altura))
        return (2 * self.base + 2 * self.altura)

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base


    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

rectangulo = Rectangulo(base=10,altura= 10)

#print(rectangulo.get_perimetro())
#print(rectangulo.get_area())



