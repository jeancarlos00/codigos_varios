import sqlite3


class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('escuela.db')

    def insertar(self, nombre, apellidos, seccion, asistencia):
        cursor = self.conexion.cursor()
        bd = """INSERT INTO datos (NOMBRE, APELLIDOS, SECCION, ASISTENCIA)
        VALUES('{}', '{}', '{}', '{}',)""".format(nombre, apellidos, seccion, asistencia)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM datos"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos

    def eliminar(self, nombre):
        cursor = self.conexion.cursor()
        bd = """DELETE FROM datos WHERE NOMBRE = '{}'""".format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualizar(self, ID, nombre, apellidos, seccion, asistencia):
        cursor = self.conexion.cursor()
        bd = '''UPDATE datos SET  NOMBRE = '{}', APELLIDOS = '{}', SECCION = '{}', ASISTENCIA = '{}'
        WHERE ID = '{}' '''.format(nombre, apellidos, seccion, asistencia, ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato


