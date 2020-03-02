import pyodbc
from Datoss.Conexion import Conexion
from Modelo.Miembro import Miembro


class MiembrosDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerMiembros(self):
        sql = "select idCliente,idAsociacion,estatus,fechaIncorporacion from Ventas.Miembros where estatus='A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql);
            data = cursor.fetchall()
            for dato in data:
                sql = "select nombre from Ventas.Clientes where idCliente=(?)"
                Values = [dato[0]]
                idC = dato[0]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[0] = row[0]
                sql = "select nombre from Ventas.Asociaciones where idAsociacion=(?)"
                Values = [dato[1]]
                idA = dato[1]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[1] = row[0]
                fila = {"idCliente":dato[0],"idAsociacion":dato[1],"estatus":dato[2],"fechaIncorporacion":dato[3],"idC":idC,"idA":idA}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarMiembro(self,miembro):
        sql = 'insert Ventas.Miembros (idCliente,idAsociacion,estatus,fechaIncorporacion) values (?,?,?,?)'
        try:
            Values = [miembro.idCliente,miembro.idAsociacion,miembro.estatus,miembro.fechaIncorporacion]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select count(*) from Ventas.Miembros"
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
    def consultaIndividual(self,idC,idA):
        sql = "select idCliente,idAsociacion,estatus,fechaIncorporacion from Ventas.Miembros where idCliente=(?) and idAsociacion=(?)"
        m=None
        try:
            cursor = self.db.cursor()
            Values = [idC,idA]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            m = Miembro(rs[0], rs[1], rs[2], rs[3])
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return m
    def actualizar(self,miembro,idC,idA):
        sql = "update Ventas.Miembros set idCliente=(?), idAsociacion=(?), estatus=(?), fechaIncorporacion=(?) " \
              "where idCliente=(?) and idAsociacion=(?)"
        try:
            cursor = self.db.cursor()
            Values = [miembro.idCliente,miembro.idAsociacion,miembro.estatus,miembro.fechaIncorporacion,idC,idA]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,idC,idA):
        sql="update Ventas.Miembros set estatus='I' where idCliente=(?) and idAsociacion=(?)"
        try:
            cursor = self.db.cursor()
            Values = [idC,idA]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)