from flask import Flask

app = Flask(__name__)

# Configuración (puedes usar un archivo config.py)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

from . import routes
