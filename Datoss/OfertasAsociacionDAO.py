import pyodbc
from Datoss.Conexion import Conexion
from Modelo.OfertaAsociacion import OfertaAsociacion


class OfertasAsociacionDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerOfertasAsociacion(self):
        sql = "select idAsociacion,idOferta,estatus from Ventas.OfertasAsociacion where estatus='A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            for dato in data:
                sql = "select nombre from Ventas.Asociaciones where idAsociacion=(?)"
                Values = [dato[0]]
                idA = dato[0]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[0] = row[0]
                sql = "select nombre from Ventas.Ofertas where idOferta=(?)"
                Values = [dato[1]]
                idO = dato[1]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[1] = row[0]
                fila = {"asociacion":dato[0],"oferta":dato[1],"estatus":dato[2],"idA":idA,"idO":idO}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarOfertaAsociacion(self,OfertaAsociacion):
        sql = 'insert Ventas.OfertasAsociacion (idAsociacion,idOferta,estatus) values (?,?,?)'
        try:
            Values = [OfertaAsociacion.idAsociacion,OfertaAsociacion.idOferta,OfertaAsociacion.estatus]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select count(*) from Ventas.OfertasAsociacion"
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
    def consultaIndividual(self,idA,idO):
        sql = "select idAsociacion,idOferta,estatus from Ventas.OfertasAsociacion where idAsociacion=(?) and idOferta=(?)"
        oa=None
        try:
            cursor = self.db.cursor()
            Values = [idA,idO]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            oa = OfertaAsociacion(rs[0], rs[1], rs[2])
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return oa
    def actualizar(self,OfertaAsociacion,idA,idO):
        sql = "update Ventas.OfertasAsociacion set idAsociacion=(?),idOferta=(?) " \
              "where idAsociacion=(?) and idOferta=(?)"
        try:
            cursor = self.db.cursor()
            Values = [OfertaAsociacion.idAsociacion,OfertaAsociacion.idOferta,idA,idO]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,idA,idO):
        sql="update Ventas.OfertasAsociacion set estatus='I' where idAsociacion=(?) and idOferta=(?)"
        try:
            cursor = self.db.cursor()
            Values = [idA,idO]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)