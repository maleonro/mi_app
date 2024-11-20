from flask import render_template
from app import app

# Cambiar el modo de depuración a False en producción
if __name__ == '__main__':
    app.run(debug=True)  # Cambia a False en producción
