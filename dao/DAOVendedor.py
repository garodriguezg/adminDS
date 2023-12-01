import pymysql

class DAOVendedor:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="proyectoDS" )
    

    def read(self, id):
        con = DAOVendedor.connect(self)
        cursor = con.cursor()
        
        try:
            if id == None:
                cursor.execute("SELECT * FROM vendedores")
            else:
                cursor.execute("SELECT * FROM vendedores where id = %s", (id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def insert(self,data):
        con = DAOVendedor.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO vendedores (usuario, correo, nombre, apellido, totalVentas, cuentaActiva, fechaCreacion) VALUES(%s, %s, %s, %s, %s, %s, %s)", (data['usuario'],data['correo'],data['nombre'],data['apellido'],data['totalVentas'],data['cuentaActiva'],data['fechaCreacion'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete(self, id):
        con = DAOVendedor.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM vendedores where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()