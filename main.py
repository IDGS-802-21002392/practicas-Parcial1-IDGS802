from flask import Flask, request, render_template
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


if __name__ =="__main__":
    app.run(debug=True)
  