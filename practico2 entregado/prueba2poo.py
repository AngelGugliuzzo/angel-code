class Persona:
    def __init__(self, nombre, apellido, edad = 20):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def caminar(self, cantidad_de_km_recorridos):
        print("Caminé " + str(cantidad_de_km_recorridos) + " kms")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def __str__(self):
        return "Nombre: {} Apellido {}".format(self.nombre, self.apellido)

    def __eq__(self, other):
        return self.nombre == other.nombre and \
               self.apellido == other.apellido

persona = Persona("Federico", "Nery")
persona2 = Persona(apellido="Nery", nombre="Federico")
print("Nombre de la persona: " + persona.nombre)
print("Apellido de la persona: " + persona.apellido)
print("Edad de la persona: " + str(persona.edad))

print("Nombre de la persona: " + persona2.nombre)
print("Apellido de la persona: " + persona2.apellido)

persona.caminar(100)

persona.nombre = "Damian"
print(persona.nombre)

persona.set_nombre("Lucas")
print(persona.get_nombre())

print("_---------------------------_")

persona_a = Persona("Angel", "Romero")
persona_b = Persona("Angel", "Romero")

print(persona_a)
print(persona_b)

print(persona_a == persona_b)