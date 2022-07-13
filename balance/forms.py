from ast import Sub
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MovimientosForm(FlaskForm):
    # ocultamos el id
    id = HiddenField
    fecha = DateField("Fecha", validators=[DataRequired(message="Debes introducir una fecha")])
    concepto = StringField("Concepto", validators=[DataRequired()])
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = FloatField("Cantidad")

    submit = SubmitField("Guardar", render_kw={ "class : blue-button" })
    