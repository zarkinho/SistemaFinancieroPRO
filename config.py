# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : config.py
# DESCRIPCIÓN:
# Configuración general de la aplicación.
# Usa SQLite en desarrollo y PostgreSQL en producción.
# ============================================================

import os

# ============================================================
# RUTAS
# ============================================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

os.makedirs(INSTANCE_DIR, exist_ok=True)

# ============================================================
# BASE DE DATOS
# ============================================================

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:

    # Compatibilidad con Render y SQLAlchemy
    if DATABASE_URL.startswith("postgres://"):

        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

else:

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            INSTANCE_DIR,
            "finanzas.db"
        )
    )

# ============================================================
# CONFIGURACIÓN
# ============================================================

class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "SistemaFinancieroPRO2026"
    )

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    SQLALCHEMY_TRACK_MODIFICATIONS = False