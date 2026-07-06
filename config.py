# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0
# ARCHIVO  : config.py
# MÓDULO   : Configuración General
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
#
# DESCRIPCIÓN:
# Este archivo contiene toda la configuración
# principal del sistema.
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

import os

# ============================================================
# RUTA DEL PROYECTO
# ============================================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ============================================================
# CONFIGURACIÓN
# ============================================================

class Config:

    # --------------------------------------------------------
    # Clave secreta
    # --------------------------------------------------------

    SECRET_KEY = "SistemaFinancieroPRO2026"

    # --------------------------------------------------------
    # Base de datos SQLite
    # --------------------------------------------------------

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            BASE_DIR,
            "instance",
            "finanzas.db"
        )
    )

    # --------------------------------------------------------
    # Desactivar advertencias
    # --------------------------------------------------------

    SQLALCHEMY_TRACK_MODIFICATIONS = False