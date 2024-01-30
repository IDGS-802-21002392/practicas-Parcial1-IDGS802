from flask import Flask, request, render_template
import forms 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")


@app.route("/resultado", methods=["GET", "POST"])
def funciones():
    value = request.form.get("op")
    if request.method =="POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))

        if value == "1":
            return f"<h1>El resultado es: '{num1+num2}'</h1>"
        elif value == "2":
            return f"<h1>El resultado es: '{num1-num2}'</h1>"
        elif value == "3":
            return f"<h1>El resultado es: '{num1*num2}'</h1>"
        elif value == "4":
           return f"<h1>El resultado es: '{num1/num2}'</h1>" 
        

@app.route("/distancia", methods=["GET", "POST"])
def index1():
    valor1 = "" 
    valor2 = ""
    valor3 = ""
    valor4 = ""

    distancia = 0  # Inicializar distancia con un valor apropiado

    distancia_form = forms.UserForm(request.form)

    if request.method == 'POST' and distancia_form.validate():
        valor1 = int(distancia_form.valor1.data)
        valor2 = int(distancia_form.valor2.data)
        valor3 = int(distancia_form.valor3.data)
        valor4 = int(distancia_form.valor4.data)

        d = valor1 - valor2
        di = valor3 - valor4
        dis = d * d
        dist = di * di
        dista = dis + dist
        distancia = dista ** 0.5

    return render_template("formularioDistancia.html", form=distancia_form, valor1=valor1, valor2=valor2, valor3=valor3, valor4=valor4, distancia=distancia)
if __name__ =="__main__":
    app.run(debug=True)
  