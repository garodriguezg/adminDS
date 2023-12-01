import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="proyectoDS" )

    def log(self, email):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT email, password from usuarios WHERE email = %s", (email,))
            return cursor.fetchone()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuarios(email, password) VALUES(%s, %s)", (data['email'],data['password'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    