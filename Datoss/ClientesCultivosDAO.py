import pyodbc
from Datoss.Conexion import Conexion
from Modelo.ClienteCultivo import ClienteCultivo


class ClientesCultivosDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerClientesCultivos(self):
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus from Ventas.ClientesCultivos" \
              " where estatus='A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            for dato in data:
                sql = "select nombre from Ventas.Clientes where idCliente=(?)"
                Values = [dato[3]]
                idC = dato[3]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[3] = row[0]
                sql = "select nombre from Ventas.Cultivos where idCultivo=(?)"
                Values = [dato[4]]
                idCu = dato[4]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[4] = row[0]
                sql = "select nombre from RH.Ciudades where idCiudad=(?)"
                Values = [dato[5]]
                idCi = dato[5]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[5] = row[0]
                fila = {"id":dato[0],"extension":dato[1],"ubicacion":dato[2],"cliente":dato[3],"cultivo":dato[4],
                        "ciudad":dato[5],"estatus":dato[6],"idC":idC,"idCu":idCu,"idCi":idCi}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarClienteCultivo(self,ClienteCultivo):
        sql = 'insert Ventas.ClientesCultivos (idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus) ' \
              'values (?,?,?,?,?,?,?)'
        try:
            Values = [ClienteCultivo.idClienteCultivo,ClienteCultivo.extension,ClienteCultivo.ubicacion,ClienteCultivo.idCliente,
                      ClienteCultivo.idCultivo,ClienteCultivo.idCiudad,ClienteCultivo.estatus]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql="select max(idClienteCultivo)+1 id from Ventas.ClientesCultivos"
        id=1
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            rs=cursor.fetchone()
            id=rs[0]
            if id == None:
               id=1
               print (id)
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return id
    def consultaIndividual(self,id):
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad from " \
              "Ventas.ClientesCultivos where idClienteCultivo=(?)"
        cc=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            cc = ClienteCultivo(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], 'A')
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return cc
    def actualizar(self,ClienteCultivo):
        sql = "update Ventas.ClientesCultivos set extension = (?),ubicacion = (?),idCliente = (?),idCultivo = (?),idCiudad = (?) " \
              "where idClienteCultivo=(?)"
        try:
            cursor = self.db.cursor()
            Values = [ClienteCultivo.extension,ClienteCultivo.ubicacion,ClienteCultivo.idCliente,
                      ClienteCultivo.idCultivo,ClienteCultivo.idCiudad,ClienteCultivo.idClienteCultivo]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,id):
        sql="update Ventas.ClientesCultivos set estatus='I' where idClienteCultivo=(?)"
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)