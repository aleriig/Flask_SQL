from ast import Sub
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField

class MovimientosForm(FlaskForm):
    # ocultamos el id
    id = HiddenField
    fecha = DateField("Fecha")
    concepto = StringField("Concepto")
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = FloatField("Cantidad")

    submit = SubmitField("Guardar", render_kw={ "class : blue-button" })
    