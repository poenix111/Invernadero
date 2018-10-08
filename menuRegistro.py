from registro import Registro
from datetime import datetime,date

class MenuRegistro:
    def __init__(self,conexion,cursor):
        self.registro = Registro(conexion,cursor)

        while True:
            print("1) Agregar registro")
            print("2) Mostrar registro")
            print("0) Salir")

            opc = input("Ingrese opcion: ")

            if(opc == "1"):
                self.insertar()

            elif (opc == "2"):
                self.mostrar()

            elif opc == "0":
                break

    def insertar(self):
        fecha = datetime.now().date()
        ph = input("INGRESE EL PH: ")
        luz = input("INGRESE LA LUZ: ")
        humedad = input("INGRESE LA HUMEDAD: ")
        co2 = input("INGRESE EL CO2: ")
        id_planta = input("ID_PLANTA: ")
        self.registro.agregar(fecha,ph,luz,humedad,co2,id_planta)
    def mostrar(self):
        id = input("INGRESE EL ID A BUSCAR: ")
        result = self.registro.recuperar(id)

        for r in result:
            print("{0:3} {1:10} {2:3} {3:3} {4:3} {5:3}" .format(r[0],str(r[1]),r[2],r[3],r[4],r[5]))