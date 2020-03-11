import pyodbc
from Datoss.Conexion import Conexion
from Modelo.Oferta import Oferta


class OfertasDAO:
    db = None
    def __init__(self):
        conx = Conexion()
        self.db = conx.getDB()
    def obtenerOfertas(self):
        sql = "select idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProducto,estatus,idProducto" \
              " from Ventas.Ofertas where estatus='A'"
        lista = []
        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            for dato in data:
                sql = "select nombre from Compras.Productos where idProducto=(?)"
                Values = [dato[8]]
                idP=dato[8]
                cursor.execute(sql, Values)
                row = cursor.fetchone()
                dato[8] = row[0]
                fila = {"idOferta":dato[0],"nombre":dato[1],"descripcion":dato[2],
                        "porDescuento":dato[3],"fechaInicio":dato[4],"fechaFin":dato[5],"canMinProducto":dato[6]
                           ,"estatus":dato[7],"Producto":dato[8],"idP":idP}
                lista.append(fila)
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
        return lista
    def insertarOferta(self,Oferta):
        sql = 'insert Ventas.Ofertas (idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProducto,estatus,idProducto)' \
              ' values (?,?,?,?,?,?,?,?,?)'
        try:
            Values = [Oferta.idOferta,Oferta.nombre,Oferta.descripcion,Oferta.porDescuento,Oferta.fechaInicio,Oferta.fechaFin,
                      Oferta.canMinProducto,Oferta.estatus,Oferta.idProducto]
            cursor=self.db.cursor()
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as error:
            print(error)
    def ultimoID(self):
        sql = "select max(idOfertas)+1 id from Ventas.Ofertas"
        id = 1
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            rs = cursor.fetchone()
            id = rs[0]
            if id == None:
                id = 1
                print (id)
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return id
    def consultaIndividual(self,id):
        sql = "select idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProducto,estatus,idProducto " \
              "from Ventas.Ofertas where idOferta=(?)"
        o=None
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql,Values)
            rs = cursor.fetchone()
            o = Oferta(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6], rs[7], rs[8])
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
        return o
    def actualizar(self,Oferta):
        sql = "update Ventas.Ofertas set nombre=(?),descripcion=(?),porDescuento=(?)," \
              "fechaInicio=(?),fechaFin=(?),canMinProducto=(?),idProducto=(?) where idOferta=(?)"
        try:
            cursor = self.db.cursor()
            Values = [Oferta.nombre,Oferta.descripcion,Oferta.porDescuento,Oferta.fechaInicio,Oferta.fechaFin,Oferta.canMinProducto,
                      Oferta.idProducto,Oferta.idOferta]
            cursor.execute(sql,Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)
    def eliminar(self,id):
        sql="update Ventas.Ofertas set estatus='I' where idOferta=(?)"
        try:
            cursor = self.db.cursor()
            Values = [id]
            cursor.execute(sql, Values)
            self.db.commit()
            cursor.close()
            self.db.close()
        except pyodbc.Error as e:
            print(e)