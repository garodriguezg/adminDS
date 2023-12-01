from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
from dao.DAOCliente import DAOCliente
from dao.DAOVendedor import DAOVendedor
from dao.DAOProducto import DAOProducto

app = Flask(__name__)
app.secret_key = "Utec"
Usuario = DAOUsuario()
Productos = DAOProducto()
Clientes = DAOCliente()
Vendedores = DAOVendedor()


@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        qwer = Usuario.log(username)
        if  password == qwer[1]:
            flash("Nice")
            # return render_template('index.html')
            return redirect(url_for('index'))
        else:
            flash("Incorrecto")
            return render_template("login.html")
    return render_template("login.html")

@app.route('/addusuario/', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if Usuario.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route("/")   
def index():
    datos = Productos.read(None)
    return render_template("index.html", data=datos)

@app.route('/updateP/<int:id>/')
def update(id):
    data = Productos.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('updateP.html', data = data)

@app.route('/updateproducto', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if Productos.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/deleteP/<int:id>/')
def delete(id):
    data = Productos.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('deleteP.html', data = data)

@app.route('/deleteproducto', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if Productos.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    

@app.route("/Ctabla.html")   
def clienteTabla():
    datos = Clientes.read(None)
    return render_template("Ctabla.html", data=datos)


@app.route("/Vtabla.html")   
def vendedorTabla():
    datos = Vendedores.read(None)
    return render_template("Vtabla.html", data = datos)


@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/actividad")
def actividad():
    return render_template("actividad.html")


if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)