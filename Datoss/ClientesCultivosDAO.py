import pyodbc
from Datoss.Conexion import Conexion
from Modelo.ClienteCultivo import ClienteCultivo


class ClientesCultivosDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerClientesCultivos(self):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        sql = "select idClienteCultivo,extension,ubicacion,estatus from Ventas.Cultivos where estatus='A'"
=======
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus from Ventas.ClientesCultivos" \
              " where estatus='A'"
>>>>>>> Stashed changes
=======
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus from Ventas.ClientesCultivos" \
              " where estatus='A'"
>>>>>>> Stashed changes
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            for dato in data:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
                fila = {"id":dato[0],"nombre":dato[1],"costoAsesoria":dato[2],"estatus":dato[3]}
=======
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                fila = {"id":dato[0],"extension":dato[1],"ubicacion":dato[2],"idCliente":dato[3],"idCultivo":dato[4],
                        "idCiudad":dato[5],"estatus":dato[6],"idC":idC,"idCu":idCu,"idCi":idCi}
>>>>>>> Stashed changes
=======
                fila = {"id":dato[0],"extension":dato[1],"ubicacion":dato[2],"cliente":dato[3],"cultivo":dato[4],
                        "ciudad":dato[5],"estatus":dato[6],"idC":idC,"idCu":idCu,"idCi":idCi}
>>>>>>> Stashed changes
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def insertarClienteCultivo(self,cultivo):
        sql = 'insert Ventas.Cultivos (idCultivo,nombre,costoAsesoria,estatus) values (?,?,?,?)'
        try:
            Values = [cultivo.idCultivo,cultivo.nombre,cultivo.costoAsesoria,cultivo.estatus]
=======
    def insertarClienteCultivo(self,ClienteCultivo):
        sql = 'insert Ventas.Cultivos (idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus) ' \
=======
    def insertarClienteCultivo(self,ClienteCultivo):
        sql = 'insert Ventas.ClientesCultivos (idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad,estatus) ' \
>>>>>>> Stashed changes
              'values (?,?,?,?,?,?,?)'
        try:
            Values = [ClienteCultivo.idClienteCultivo,ClienteCultivo.extension,ClienteCultivo.ubicacion,ClienteCultivo.idCliente,
                      ClienteCultivo.idCultivo,ClienteCultivo.idCiudad,ClienteCultivo.estatus]
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        sql="select max(idCultivo)+1 id from Ventas.Cultivos"
=======
        sql="select max(idClienteCultivo)+1 id from Ventas.ClientesCultivos"
>>>>>>> Stashed changes
=======
        sql="select max(idClienteCultivo)+1 id from Ventas.ClientesCultivos"
>>>>>>> Stashed changes
        id=1
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            rs=cursor.fetchone()
            id=rs[0]
<<<<<<< Updated upstream
=======
            if id == None:
               id=1
               print (id)
>>>>>>> Stashed changes
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return id
    def consultaIndividual(self,id):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        sql = "select idCultivo,nombre,costoAsesoria,estatus from Ventas.Cultivos where idCultivo=(?)"
        c=None
=======
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad from " \
              "Ventas.ClientesCultivos where idClienteCultivo=(?)"
        cc=None
>>>>>>> Stashed changes
=======
        sql = "select idClienteCultivo,extension,ubicacion,idCliente,idCultivo,idCiudad from " \
              "Ventas.ClientesCultivos where idClienteCultivo=(?)"
        cc=None
>>>>>>> Stashed changes
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            c = Cultivo(rs[0], rs[1], rs[2], rs[3])
=======
            cc = ClienteCultivo(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], 'A')
>>>>>>> Stashed changes
=======
            cc = ClienteCultivo(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], 'A')
>>>>>>> Stashed changes
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        return c
    def actualizar(self,cultivo):
        sql = "update Ventas.Cultivos set nombre=(?), costoAsesoria=(?), estatus=(?) where idCultivo=(?)"
        try:
            cursor = self.db.cursor()
            Values = [cultivo.nombre, cultivo.costoAsesoria, cultivo.estatus, cultivo.idCultivo]
=======
=======
>>>>>>> Stashed changes
        return cc
    def actualizar(self,ClienteCultivo):
        sql = "update Ventas.ClientesCultivos set extension = (?),ubicacion = (?),idCliente = (?),idCultivo = (?),idCiudad = (?) " \
              "where idClienteCultivo=(?)"
        try:
            cursor = self.db.cursor()
            Values = [ClienteCultivo.extension,ClienteCultivo.ubicacion,ClienteCultivo.idCliente,
                      ClienteCultivo.idCultivo,ClienteCultivo.idCiudad,ClienteCultivo.idClienteCultivo]
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,id):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        sql="update Ventas.Cultivos set estatus='I' where idCultivo=(?)"
=======
        sql="update Ventas.ClientesCultivos set estatus='I' where idClienteCultivo=(?)"
>>>>>>> Stashed changes
=======
        sql="update Ventas.ClientesCultivos set estatus='I' where idClienteCultivo=(?)"
>>>>>>> Stashed changes
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)