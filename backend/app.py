# backend/app.py

from flask import Flask
from flask_cors import CORS
from controllers.cliente import cliente_bp
from controllers.orden import orden_bp
from controllers.inventario import inventario_bp
from controllers.trabajador import trabajador_bp
from controllers.orden_inv import orden_inv_bp

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir acceso desde frontend

app.register_blueprint(cliente_bp)
app.register_blueprint(orden_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(trabajador_bp)
app.register_blueprint(orden_inv_bp)

if __name__ == '__main__':
    app.run(debug=True)
