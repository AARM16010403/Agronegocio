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
    def insertarCultivo(self,cultivo):
        sql = 'insert Ventas.Cultivos (idCultivo,nombre,costoAsesoria,estatus) values (?,?,?,?)'
        try:
            Values = [cultivo.idCultivo,cultivo.nombre,cultivo.costoAsesoria,cultivo.estatus]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select max(idCultivo)+1 id from Ventas.Cultivos"
        id=1
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            rs=cursor.fetchone()
            id=rs[0]
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return id
    def consultaIndividual(self,id):
        sql = "select idCultivo,nombre,costoAsesoria,estatus from Ventas.Cultivos where idCultivo=(?)"
        c=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            c = Cultivo(rs[0], rs[1], rs[2], rs[3])
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return c
    def actualizar(self,cultivo):
        sql = "update Ventas.Cultivos set nombre=(?), costoAsesoria=(?), estatus=(?) where idCultivo=(?)"
        try:
            cursor = self.db.cursor()
            Values = [cultivo.nombre, cultivo.costoAsesoria, cultivo.estatus, cultivo.idCultivo]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
