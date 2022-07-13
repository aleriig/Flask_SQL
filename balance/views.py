from datetime import date

from flask import render_template, request

from . import app
from .forms import MovimientosForm
from .models import DBManager


RUTA = 'data/balance.db'


@app.route("/")
def inicio():
    """
    Muestra la lista de movimientos cargados.
    """
    db = DBManager(RUTA)
    movimientos = db.consulta_SQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Crear movimiento"


@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    if request.method == "GET":
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimientoPorId(id)

        print("ANTES:", movimiento["fecha"])
        movimiento["fecha"] = date.fromisoformat(movimiento["fecha"])

        formulario = MovimientosForm(data=movimiento)
        return render_template("form_movimiento.html", form=formulario, id=id)

    elif request.method == "POST":
        form = MovimientosForm(data=request.form)
        if form.validate():
            return "Guardo los datos"
        return "El formulario tiene errores"

        


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db = DBManager(RUTA)
    # esta_borrado = db.borrar(id)
    consulta = "DELETE FROM movimientos WHERE id=?"
    params = (id,)
    esta_borrado = db.consulta_con_parametros(consulta, params)
    return render_template("borrar.html", resultado=esta_borrado)