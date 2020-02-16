import pyodbc

class Conexion:
    db=None
    def __init__(self):
        self.db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                +'DESKTOP-G0GC4F8'
                                +';DATABASE='
                                +'ERP2020'+';UID='+'DBA'+';PWD='+'qwerty')
    def getDB(self):
        return self.db
    def cerrarDB(self):
        self.db.close()
