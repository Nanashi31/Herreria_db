# backend/controllers/orden.py

from flask import Blueprint, request, jsonify
from db_config import get_connection

orden_bp = Blueprint('orden', __name__)

@orden_bp.route('/ordenes', methods=['GET'])
def obtener_ordenes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orden")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@orden_bp.route('/ordenes/<int:id>', methods=['GET'])
def obtener_orden(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orden WHERE Id_Ord = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@orden_bp.route('/ordenes', methods=['POST'])
def agregar_orden():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orden (Id_Ord, Tipo, Presupuesto, Id_Cliente, Fecha) VALUES (%s, %s, %s, %s, %s)",
                   (datos['Id_Ord'], datos['Tipo'], datos['Presupuesto'], datos['Id_Cliente'], datos['Fecha']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Orden agregada correctamente'}), 201

@orden_bp.route('/ordenes/<int:id>', methods=['PUT'])
def actualizar_orden(id):
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orden SET Tipo=%s, Presupuesto=%s, Id_Cliente=%s, Fecha=%s WHERE Id_Ord = %s",
                   (datos['Tipo'], datos['Presupuesto'], datos['Id_Cliente'], datos['Fecha'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Orden actualizada correctamente'})

@orden_bp.route('/ordenes/<int:id>', methods=['DELETE'])
def eliminar_orden(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orden WHERE Id_Ord = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Orden eliminada correctamente'})
