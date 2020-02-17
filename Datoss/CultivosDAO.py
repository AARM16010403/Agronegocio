import pyodbc
from Datoss.Conexion import Conexion
from Modelo.Cultivo import Cultivo


class CultivosDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerCultivos(self):
        sql = 'select idCultivo,nombre,costoAsesoria,estatus from Ventas.Cultivos'
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql);
            data = cursor.fetchall()
            for dato in data:
                fila = {"id":dato[0],"nombre":dato[1],"costoAsesoria":dato[2],"estatus":dato[3]}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista