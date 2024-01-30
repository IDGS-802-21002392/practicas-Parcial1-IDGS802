from wtforms import Form, IntegerField

class UserForm(Form):
    valor1 = IntegerField("valor de X1")
    valor2 = IntegerField("valor de X2")
    valor3 = IntegerField('valor de Y1')
    valor4 = IntegerField('valor de Y3')
