# backend/controllers/inventario.py

from flask import Blueprint, request, jsonify
from db_config import get_connection

inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/inventario', methods=['GET'])
def obtener_materiales():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventario")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@inventario_bp.route('/inventario/<int:id>', methods=['GET'])
def obtener_material(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventario WHERE Id_Mat = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@inventario_bp.route('/inventario', methods=['POST'])
def agregar_material():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventario (Id_Mat, Nombre, Precio, Tipo) VALUES (%s, %s, %s, %s)",
                   (datos['Id_Mat'], datos['Nombre'], datos['Precio'], datos['Tipo']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Material agregado correctamente'}), 201

@inventario_bp.route('/inventario/<int:id>', methods=['PUT'])
def actualizar_material(id):
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventario SET Nombre=%s, Precio=%s, Tipo=%s WHERE Id_Mat = %s",
                   (datos['Nombre'], datos['Precio'], datos['Tipo'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Material actualizado correctamente'})

@inventario_bp.route('/inventario/<int:id>', methods=['DELETE'])
def eliminar_material(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventario WHERE Id_Mat = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Material eliminado correctamente'})
