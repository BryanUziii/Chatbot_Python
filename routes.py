from flask import Blueprint, render_template, request
from modules.chatbot import procesar_entrada

my_blueprint = Blueprint('my_blueprint', __name__)

# rutas para renderizar las paginas
@my_blueprint.route('/')
def index():
    return render_template('index.html')

# rutas para interactuar con el chatbot
@my_blueprint.route('/chatbot', methods=['POST'])
def chatbot():
    entrada = request.form.get('entrada')
    respuesta = procesar_entrada(entrada)
    return respuesta
