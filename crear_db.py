# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0
# ARCHIVO  : crear_db.py
# MÓDULO   : Creación de la Base de Datos
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
#
# DESCRIPCIÓN:
#
# Este archivo crea automáticamente todas las tablas
# definidas en models.py.
#
# Solo se ejecuta la primera vez o cuando iniciemos
# un proyecto nuevo.
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

from app import create_app
from app import db

# ============================================================
# CREAR APLICACIÓN
# ============================================================

app = create_app()

# ============================================================
# CREAR BASE DE DATOS
# ============================================================

with app.app_context():

    db.create_all()

    print("=" * 60)
    print("✅ Base de datos creada correctamente.")
    print("=" * 60)