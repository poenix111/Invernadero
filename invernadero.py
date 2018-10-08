class Invernadero:
    def __init__(self,conexion,cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crear(self,nombre,ubicacion,id_dueno):
        try:
            insertar = ("INSERT INTO invernadero(nombre,ubicacion,id_dueno) VALUE(%s,%s,%s)")
            self.cursor.execute(insertar,(nombre,ubicacion,id_dueno))
            self.conexion.commit()
        except:
            print("OCURRIO ALGO AL INTENTAR INSERTAR")
    def recuperar(self):
        select = ("SELECT * FROM invernadero")
        self.cursor.execute(select)
        return self.cursor.fetchall()