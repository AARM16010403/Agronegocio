import pyodbc

class Conexion:
    db=None
    def __init__(self):
        db=None
        self.db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                 + 'DESKTOP-G0GC4F8'
                                 + ';DATABASE='
                                 + 'ERP2020' + ';UID=DBA;PWD=qwerty')
    def verificarUsuario(self,us,co):
        res = True
        try:
            self.db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                     + 'DESKTOP-G0GC4F8'
                                     + ';DATABASE='
                                     + 'ERP2020' + ';UID=' + str(us) + ';PWD=' + str(co))
        except pyodbc.Error as error:
            print(error)
            res = False
        return res
    def getDB(self):
        return self.db
    def cerrarDB(self):
        self.db.close()


# class Conexion:
#     db=None
#     def __init__(self):
#         self.db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
#                                 +'DESKTOP-G0GC4F8'
#                                 +';DATABASE='
#                                 +'ERP2020'+';UID='+'DBA'+';PWD='+'qwerty')
#     def getDB(self):
#         return self.db
#     def cerrarDB(self):
#         self.db.close()
