from invernadero import Invernadero

class MenuInvernadero:
    def __init__(self,conexion,cursor):
        self.inv = Invernadero(conexion,cursor)
        while True:
            print("1) Agregar invernadero")
            print("2) Mostrar invernaderos")
            print("0) Salir")

            opc = input("Ingrese opcion: ")

            if(opc == "1"):
                self.agregar()

            elif (opc == "2"):
                self.mostrar()

            elif opc == "0":
                break
            

    def agregar(self):
        nombre = input("Nombre invernadero: ")
        ubicacion = input("Ubicacion: ")
        id_dueno = input("id_dueno: ")
        self.inv.crear(nombre,ubicacion,id_dueno)

    def mostrar(self):
        resultados = self.inv.recuperar()

        for r in resultados:
            print("{0:3} {1:10} {2:10} {3:3}" .format(r[0],r[1],r[2],r[3]))