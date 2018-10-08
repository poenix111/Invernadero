from usuario import Usuario
import getpass

class MenuUsuario:

    def __init__(self,conexion, cursor):
        self.usuario = Usuario(conexion,cursor)
        self.conexion = conexion
        self.cursor = cursor

        while True:
            print("1) Agregar Usuario")
            print("2) LOGIN")
            print("0) Salir")

            opc = input("Ingrese opcion: ")

            if(opc == "1"):
                self.capturar()
            elif (opc == '2'):
                self.login()
            elif opc == "0":
                break

    def capturar(self):
        correo = input("Correo: ")
        password = getpass.getpass("Contraseña: ")
        tipo = input("Tipo: ")
        self.usuario.crear(correo,password,tipo)

    def login(self):
        correo = input("Correo: ")
        password = getpass.getpass("Contraseña: ")
        if self.usuario.login(correo,password):
            print("Bienvenido")
        else:
            print("Usuario/Contraseña incorrectos")

        