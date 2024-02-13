from flask import Flask, request, render_template
import forms
from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, SubmitField
import signo
import datetime
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

@app.route('/signoChino', methods=['GET', 'POST'])
def calSigno():
    form = signo.UserForm(request.form)
    nombre = ""
    apaterno =""
    amaterno = ""
    dia = 0
    mes = 0
    anio = 0
    sexo = ""
    if request.method == 'POST':
        nombre = form.nombre.data
        apaterno = form.apaterno.data
        amaterno = form.amaterno.data
        dia = form.dia.data
        mes = form.mes.data
        anio = form.anio.data
        sexo = form.sexo.data
        s, edad = calcular_signo(anio)
        return render_template('resultado.html', signo = s, nombre=nombre, apaterno=apaterno, amaterno=amaterno, anio = anio, edad = edad)
        
    return render_template('formularioSigno.html', form=form, nombre=nombre, apaterno = apaterno, amaterno=amaterno, dia = dia, mes=mes, sexo = sexo)

def calcular_signo(anio):
    signos = {"Rata":[1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020], 
              "Buey": [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021], 
              "Tigre":[1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022], 
              "Conejo":[1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
              "Dragon":[1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
              "Serpiente":[1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
              "Caballo":[1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026],
              "Cabra":[1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027],
              "Mono":[1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028],
              "Gallo": [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029],
              "Perro":[1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]}
    s = 0
    edad = datetime.datetime.now().year - anio
    for signo, a in signos.items():
        if anio in a:
            s = signo
    return s, edad
if __name__ =="__main__":
    app.run(debug=True)
  