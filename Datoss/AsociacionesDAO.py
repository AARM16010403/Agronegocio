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
    def insertarAsociacion(self,asociacion):
        sql = 'insert Ventas.Asociaciones (idAsociacion,nombre,estatus) values (?,?,?)'
        try:
            Values = [asociacion.idAsociacion,asociacion.nombre,asociacion.estatus]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select max(idAsociacion)+1 id from Ventas.Asociaciones"
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
        sql = "select idAsociacion,nombre,estatus from Ventas.Asociaciones where idAsociacion=(?)"
        a=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            a = Asociacion(rs[0], rs[1], rs[2])
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return a
    def actualizar(self,asociacion):
        sql = "update Ventas.Asociaciones set nombre=(?), estatus=(?) where idAsociacion=(?)"
        try:
            cursor = self.db.cursor()
            Values = [asociacion.nombre, asociacion.estatus, asociacion.idAsociacion]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)