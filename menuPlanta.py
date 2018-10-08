from planta import Planta
from datetime import datetime,date
class MenuPlanta:

    def __init__(self,conexion, cursor):
        self.planta = Planta(conexion,cursor)
        self.conexion = conexion
        self.cursor = cursor

        while True:
            print("1) Agregar planta")
            print("2) Mostrar")
            print("0) Salir")

            opc = input("Ingrese opcion: ")

            if(opc == "1"):
                self.agregar()
            elif(opc == '2'):
                self.mostrar()
            elif opc == "0":
                break

    def agregar(self):
        cultivo = input("Ingrese el nombre del cultivo: ")
        fecha = datetime.now().date()
        #dia = input("dia: ")
        #mes = input("mes: ")
        #year = input("año: ")
        #fecha = date(int(year),int(mes),int(dia))
        id_clasi = input("ID_CLASI: ")
        id_inv = input("ID_INVERNADERO: ")
        self.planta.agregar(cultivo,fecha,id_clasi,id_inv)

    def mostrar(self):
        buscar = input("id_inv: ")
        lista = self.planta.recuperar(buscar)
        for name in lista:
            print("{0:2} {1:10} {2:10}" .format(name[0],name[1], str(name[2])))