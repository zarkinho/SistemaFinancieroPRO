# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : config.py
# ============================================================

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_DIR = os.path.join(BASE_DIR, "instance")

os.makedirs(INSTANCE_DIR, exist_ok=True)


class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "SistemaFinancieroPRO2026"
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(
            INSTANCE_DIR,
            "finanzas.db"
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False