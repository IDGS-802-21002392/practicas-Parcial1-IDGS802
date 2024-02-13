from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms import Form, IntegerField

class UserForm(Form):
    nombre = StringField('Nombre')
    apaterno = StringField('Apellido paterno')
    amaterno = StringField('Apellido materno')
    dia = IntegerField('Día de nacimiento')
    mes = IntegerField('Mes de nacimiento')
    anio = IntegerField('Año de nacimiento')
    sexo = RadioField('Sexo', choices=[('Masculino'), ('Femenino')])
    submit = SubmitField('Calcular')

