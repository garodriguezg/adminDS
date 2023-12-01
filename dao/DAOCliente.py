import pymysql

class DAOCliente:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="proyectoDS" )

    def read(self, id):
        con = DAOCliente.connect(self)
        cursor = con.cursor()
        
        try:
            if id == None:
                cursor.execute("SELECT * FROM clientes")
            else:
                cursor.execute("SELECT * FROM clientes where id = %s", (id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def insert(self,data):
        con = DAOCliente.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO clientes(usuario, correo, nombre, apellido, totalCompras, cuentaActiva, fechaCreacion) VALUES(%s, %s, %s, %s, %s, %s, %s)", (data['usuario'],data['correo'],data['nombre'],data['apellido'],data['totalCompras'],data['cuentaActiva'],data['fechaCreacion'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete(self, id):
        con = DAOCliente.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM clientes where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
