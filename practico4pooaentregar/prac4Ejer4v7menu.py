#4.	Nos piden realizar una agenda telefónica de contactos.

#a.	Un contacto está definido por un nombre y un teléfono (No es necesario de validar).
# Un contacto es igual a otro cuando sus nombres son iguales.

#b.	Una agenda de contactos está formada por un conjunto de contactos (Piensa en que tipo puede ser)

#c.	Se podrá crear de dos formas, indicándoles nosotros el tamaño o con un tamaño por defecto (10)

# d.	Los métodos de la agenda serán los siguientes:
# i.	aniadirContacto(Contacto c): Añade un contacto a la agenda, sino se pueden meter más
#       a la agenda se indicara por pantalla. No se pueden meter contactos que existan, es decir, no podemos duplicar
#       nombres, aunque tengan distinto teléfono.
# ii.	existeContacto(Conctacto c): indica si el contacto pasado existe o no.
# iii.	listarContactos(): Lista toda la agenda
# iv.	buscaContacto(String nombre): busca un contacto por su nombre y muestra su teléfono.
# v.	eliminarContacto(Contacto c): elimina el contacto de la agenda, indica si se ha eliminado o no por pantalla
# vi.	agendaLlena(): indica si la agenda está llena.
# vii.	huecosLibres(): indica cuantos contactos más podemos meter.
#e.	Crea un menú con opciones por consola para probar todas estas funcionalidades.


class Contacto:
    def __init__(self, nombre, apellido, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono

class Agenda:
    def __init__(self):
        self.contactos = []
        self.LARGO_DE_AGENDA=11

    def añadir_contacto(self, nombre, telefono):
        contacto = Contacto(" "," ",0)
        contacto.nombre = nombre
        # contacto.apellido =
        contacto.telefono = telefono
        self.contactos.append(contacto)

    def existeContacto(self,nombre):
        for contacto in self.contactos: #---------------->lo saque del def imprimir
            if contacto.nombre == nombre:
                print("contacto existe")

    def buscaContacto(self,nombre): #------------------>tomar carta
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("contacto existe")
                print(contacto.telefono)

    def imprimir(self):
        for contacto in self.contactos:
            print(contacto.nombre, contacto.apellido, contacto.telefono)

    def eliminarContacto(self,nombre):
        contador=0
        for contacto in self.contactos:
            contador += 1
            if contacto.nombre == nombre:
                self.contactos.pop(contador) #------------>no hace la baja

    def agendaLlena(self):
        if len(self.contactos)<=self.LARGO_DE_AGENDA:
            return "hay espacio"#----------->con lugar
        else:
            return "lleno"  #----------->lleno

    def huecosLibres(self):
        libres=self.LARGO_DE_AGENDA-len(self.contactos)
        return libres

#___________________________________________________________________________________________________________
agenda =Agenda()
agenda.añadir_contacto(" ",0)
control_Ciclo = True
while control_Ciclo:
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("° 1_INGRESE UN CONTACTO     °")
    print("° 2_BUSCAR UN CONTACTO      °")
    print("° 3_BORRAR UN CONTACTO      °")
    print("° 4_ESPACIO DISPONIBLE      °")
    print("° 5_LISTAR LA AGENDA        °")
    print("° 6_CANTIDAD DE DISPONIBLES °")
    print("° 7_SALIR DEL MENU          °")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    numeroDeEleccion = int(input("ingrese su eleccion:"))
    if numeroDeEleccion == 1:
        nombre=str(input("ingrese nombre : "))
        numero=int(input("ingrese numero de telefono : "))
        agenda.añadir_contacto(nombre, numero)
    if numeroDeEleccion == 2:
        nombre = str(input("ingrese nombre : "))
        agenda.buscaContacto(nombre)
    if numeroDeEleccion == 3:
        nombre = str(input("ingrese nombre : "))
        agenda.eliminarContacto(nombre)
    if numeroDeEleccion == 4:
        print((agenda.agendaLlena()))
    if numeroDeEleccion == 5:
        agenda.imprimir()
    if numeroDeEleccion == 6:
        print(agenda.huecosLibres())
    if numeroDeEleccion == 7:
        control_Ciclo = False
        print("adiosssssss")



