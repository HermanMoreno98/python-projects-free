from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predecir", methods=["POST"])
def predecir():
    cuartos = int(request.form["cuartos"])
    distancia = int(request.form["distancia"])
    prediccion = model.predict([[cuartos,distancia]])
    output = round(prediccion[0],2)
    return render_template("index.html", prediccion_texto=f"La casa con {cuartos} cuartos y localizado a {distancia} km tiene un valor de ${output}K")

if __name__ == "__main__":
    app.run()
   
 