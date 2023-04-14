from flask import Flask, render_template, request
import openai
import json

app = Flask(__name__)

# Lee la clave de la API desde el archivo JSON
with open('keys.json', 'r') as f:
    keys = json.load(f)
    api_key = keys['api_key']

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/generate_report', methods=['POST'])
def generate_report():
    # Obtener los datos del formulario
    title = request.form['title']
    summary = request.form['summary']
    
    # Conectar con el modelo GPT de OpenAI para generar el texto
    prompt = f"Titulo: {title}\Resumen: {summary}\nGenera un reporte que resuma el siguiente articulo:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.7,
    )
    body = response.choices[0].text
    
    return render_template("index.html", prediccion_texto=f"El resumen se presenta a continuación:\n{body}")


if __name__ == "__main__":
    app.run()