import mysql.connector

conexion = mysql.connector.connect(user="brian",password="12345",database="invernadero")

cursor = conexion.cursor()

insertar = ('INSERT INTO dueno(nombre, apellidos)VALUES("Brian","Munoz")')

cursor.execute(insertar)

conexion.commit()