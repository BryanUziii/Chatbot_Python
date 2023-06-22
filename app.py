from flask import Flask, render_template, request
from modules.chatbot import procesar_entrada

app = Flask(__name__)

# Rutas para renderizar las páginas
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para interactuar con el chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    entrada = request.form.get('entrada')
    respuesta = procesar_entrada(entrada)
    return respuesta


if __name__ == '__main__':
    app.run()

