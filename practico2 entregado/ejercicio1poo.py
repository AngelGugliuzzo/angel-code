
#1.	Crear una clase Rectángulo que tenga
#a.	Los atributos base y altura.
#b.	Crear el constructor de la clase que reciba por argumento los valores de la base y la altura.
#c.	Los métodos necesarios para:
#i.	Calcular el área. La fórmula es base*altura
#ii.	El perímetro. La formula es 2*base + 2*altura

class rectangulo1:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def superficie(self,base,altura):
        print("superficie " + str(base * altura) + " ms")

    def perimetro(self,base,altura):
        print("perimetro " + str(2*base +2*altura) + " ms")


dimenciones = rectangulo1(10, 10)
print("base: ", dimenciones.base)
print("altura:", dimenciones.altura)
dimenciones.superficie(10,10)
dimenciones.perimetro(10,10)



#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[0]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
class rectangulo2:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.perimetro=(2*base+2*altura)
        self.superficie=(base*altura)

dimenciones=rectangulo2(10,10)
print("perimetro :"+str(dimenciones.perimetro)+" "+str(dimenciones.superficie))
print("perimetro: ",dimenciones.perimetro,"metros")#-------------------->el numero como entero
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]