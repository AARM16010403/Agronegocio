import pyodbc
from Datoss.Conexion import Conexion
from Modelo.Asociacion import Asociacion


class AsociacionesDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerAsociaciones(self):
        sql = 'select idAsociacion,nombre,estatus from Ventas.Asociaciones'
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql);
            data = cursor.fetchall()
            for dato in data:
                fila = {"id":dato[0],"nombre":dato[1],"estatus":dato[2]}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista