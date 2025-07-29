# backend/controllers/cliente.py

from flask import Blueprint, request, jsonify
from db_config import get_connection

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente WHERE Id_Cli = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@cliente_bp.route('/clientes', methods=['POST'])
def agregar_cliente():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cliente (Id_Cli, Nom, ApP, ApM, Cel, Dire) VALUES (%s, %s, %s, %s, %s, %s)",
                   (datos['Id_Cli'], datos['Nom'], datos['ApP'], datos['ApM'], datos['Cel'], datos['Dire']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Cliente agregado correctamente'}), 201

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE cliente SET Nom=%s, ApP=%s, ApM=%s, Cel=%s, Dire=%s WHERE Id_Cli = %s",
                   (datos['Nom'], datos['ApP'], datos['ApM'], datos['Cel'], datos['Dire'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Cliente actualizado correctamente'})

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliente WHERE Id_Cli = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Cliente eliminado correctamente'})
