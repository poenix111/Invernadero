import mysql.connector
from dueno import Dueno
from menuDueno import MenuDueno
from menuInvernadero import MenuInvernadero
from menuUsuario import MenuUsuario
from menuPlanta import MenuPlanta
from menuRegistro import MenuRegistro
conexion = mysql.connector.connect(user="brian",password="12345",database="invernadero")

cursor = conexion.cursor()

while True:
    print("1) Menu dueño")
    print("2) Menu Invernadero")
    print("3) Menu Usuario")
    print("4) Menu Planta")
    print("5) Menu REGISTRO")    


    print("0) Salir")

    opc = input("Ingrese su opcion: ")

    if (opc == "1"):
        menuD = MenuDueno(conexion,cursor)
    elif (opc == "2"):
        menuI = MenuInvernadero(conexion,cursor)
    elif(opc == '3'):
        menuU = MenuUsuario(conexion,cursor)
    elif(opc == '4'):
        menuP = MenuPlanta(conexion,cursor)
    elif(opc == '5'):
        menuR = MenuRegistro(conexion,cursor)
    elif (opc == "0"):
        break

"""
d = Dueno(conexion,cursor)

d.crear('Paul','Trapito')

print(d.recuperar())
"""
