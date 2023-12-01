import pymysql

class DAOProducto:
    def connect(self):
        return pymysql.connect(host='localhost', user="root", password="", db='proyectoDS')
    
    def read(self, id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()
        
        try:
            if id == None:
                cursor.execute("SELECT * FROM productos")
            else:
                cursor.execute("SELECT * FROM productos where id = %s", (id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()

    def update(self, id, data):
            con = DAOProducto.connect(self)
            cursor = con.cursor()

            try:
                cursor.execute("UPDATE productos set producto = %s, fecha_inicio = %s, realizada = %s, fecha_fin = %s,  precio = %s, satisfecho = %s, codigo = %s  where id = %s", (data['producto'],data['fecha_inicio'],data['realiada'],data['fecha_fin'],data['precio'],data['satisfecho'],data['codigo'],id,))
                con.commit()
                return True
            except:
                con.rollback()
                return False
            finally:
                con.close()

    def delete(self, id):
            con = DAOProducto.connect(self)
            cursor = con.cursor()

            try:
                cursor.execute("DELETE FROM productos where id = %s", (id,))
                con.commit()
                return True
            except:
                con.rollback()
                return False
            finally:
                con.close()