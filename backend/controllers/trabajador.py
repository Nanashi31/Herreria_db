# backend/controllers/trabajador.py

from flask import Blueprint, request, jsonify
from db_config import get_connection

trabajador_bp = Blueprint('trabajador', __name__)

@trabajador_bp.route('/trabajadores', methods=['GET'])
def obtener_trabajadores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM trabajador")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@trabajador_bp.route('/trabajadores/<int:id>', methods=['GET'])
def obtener_trabajador(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM trabajador WHERE Id_Tra = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(resultado)

@trabajador_bp.route('/trabajadores', methods=['POST'])
def agregar_trabajador():
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trabajador (Id_Tra, Nom, ApP, ApM, Correo, Tel, Fec_Nac) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (datos['Id_Tra'], datos['Nom'], datos['ApP'], datos['ApM'], datos['Correo'], datos['Tel'], datos['Fec_Nac'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Trabajador agregado correctamente'}), 201

@trabajador_bp.route('/trabajadores/<int:id>', methods=['PUT'])
def actualizar_trabajador(id):
    datos = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE trabajador SET Nom=%s, ApP=%s, ApM=%s, Correo=%s, Tel=%s, Fec_Nac=%s WHERE Id_Tra = %s",
        (datos['Nom'], datos['ApP'], datos['ApM'], datos['Correo'], datos['Tel'], datos['Fec_Nac'], id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Trabajador actualizado correctamente'})

@trabajador_bp.route('/trabajadores/<int:id>', methods=['DELETE'])
def eliminar_trabajador(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trabajador WHERE Id_Tra = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensaje': 'Trabajador eliminado correctamente'})
