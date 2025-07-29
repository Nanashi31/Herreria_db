# backend/controllers/orden_inv.py

from flask import Blueprint, request, jsonify
from db_config import get_connection

orden_inv_bp = Blueprint('orden_inv', __name__)

@orden_inv_bp.route('/ordenes-materiales', methods=['GET'])
def obtener_todo():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orden_inv")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@orden_inv_bp.route('/ordenes-materiales/<int:orden_id>', methods=['GET'])
def materiales_de_orden(orden_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT oi.Id_Mat, i.Nombre, oi.Usado
        FROM orden_inv oi
        JOIN inventario i ON oi.Id_Mat = i.Id_Mat
        WHERE oi.Id_Ord = %s
    """, (orden_id,))
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@orden_inv_bp.route('/ordenes-materiales', methods=['POST'])
def agregar_material_a_orden():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orden_inv (Id_Ord, Id_Mat, Usado) VALUES (%s, %s, %s)",
                   (datos['Id_Ord'], datos['Id_Mat'], datos['Usado']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Material agregado a orden correctamente'}), 201

@orden_inv_bp.route('/ordenes-materiales', methods=['PUT'])
def actualizar_usado():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orden_inv SET Usado = %s WHERE Id_Ord = %s AND Id_Mat = %s",
                   (datos['Usado'], datos['Id_Ord'], datos['Id_Mat']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Cantidad actualizada correctamente'})

@orden_inv_bp.route('/ordenes-materiales', methods=['DELETE'])
def eliminar_material_de_orden():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orden_inv WHERE Id_Ord = %s AND Id_Mat = %s",
                   (datos['Id_Ord'], datos['Id_Mat']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Material eliminado de la orden'})
