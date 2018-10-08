from dueno import Dueno

class MenuDueno:
    def __init__(self,conexion,cursor):
        self.dueno = Dueno(conexion,cursor)
        
        while True:
            print("1) Agregar Dueño")
            print("2) Mostrar Dueño")
            print("0) Salir")

            opc = input("Ingrese su opcion: ")

            if(opc == "1"):
               self.agregar()
            elif (opc == "2"):
                self.mostrar()
            elif (opc == "0"):
                break

    def agregar(self):
        nombre = input("Nombre : ")
        apellidos = input("Apellidos : ")
        self.dueno.crear(nombre,apellidos)

    def mostrar(self):
        resultados = self.dueno.recuperar()

        for r in resultados:
            print("{0:3} {1:10} {2:15}".format(r[0],r[1],r[2]))