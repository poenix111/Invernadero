

class Planta:
    def __init__(self,conexion,cursor):
        self.conexion = conexion
        self.cursor = cursor

    def agregar(self,cultivo,fecha,id_clasi,id_inv):
        insertar = ("INSERT INTO planta(cultivo,fecha,id_clasi,id_inv) VALUES(%s,%s,%s,%s)")
        self.cursor.execute(insertar,(cultivo,fecha,id_clasi,id_inv))
        self.conexion.commit()

    def recuperar(self,id_inv):
        buscar = ("SELECT * FROM planta WHERE id_inv = %s")
        self.cursor.execute(buscar,(id_inv,))
        return self.cursor.fetchall()