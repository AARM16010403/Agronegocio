import pyodbc
from Datoss.Conexion import Conexion
from Modelo.UnidadTrans import UnidadTrans


class UnidadesTransDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerUnidades(self):
        sql = "select idUnidadTransporte,placas,marca,modelo,anio,capacidad from Ventas.UnidadesTransporte where estatus='A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql);
            data = cursor.fetchall()
            for dato in data:
                fila = {"id":dato[0],"placa":dato[1],"marca":dato[2],"modelo":dato[3],"anio":dato[4],"capacidad":dato[5]}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarUnidad(self,unidad):
        sql = 'insert Ventas.UnidadesTransporte (idUnidadTransporte,placas,marca,modelo,anio,capacidad,estatus) values (?,?,?,?,?,?,?)'
        try:
            Values = [unidad.idUnidadTransporte,unidad.placas,unidad.marca,unidad.modelo,unidad.anio,unidad.capacidad,unidad.estatus]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select max(idUnidadTransporte)+1 id from Ventas.UnidadesTransporte"
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
        sql = "select idUnidadTransporte,placas,marca,modelo,anio,capacidad from Ventas.UnidadesTransporte" \
              " where idUnidadTransporte=(?)"
        u=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            u = UnidadTrans(rs[0], rs[1], rs[2], rs[3],rs[4],rs[5],'A')
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return u
    def actualizar(self,unidad):
        sql = "update Ventas.UnidadesTransporte set placas=(?), marca=(?), modelo=(?), anio=(?), capacidad=(?) " \
              "where idUnidadTransporte=(?)"
        try:
            cursor = self.db.cursor()
            Values = [unidad.placas,unidad.marca,unidad.modelo,unidad.anio,unidad.capacidad,unidad.idUnidadTransporte]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,id):
        sql="update Ventas.UnidadesTransporte set estatus='I' where idUnidadTransporte=(?)"
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)