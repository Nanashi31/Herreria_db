# backend/db_config.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # ← cambia si usas otro usuario
        password="1234",            # ← pon tu contraseña si tienes
        database="herreriadb"
    )
