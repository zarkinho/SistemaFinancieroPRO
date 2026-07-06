# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0
# ARCHIVO  : __init__.py
# MÓDULO   : Inicialización de la aplicación
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ============================================================
# OBJETOS GLOBALES
# ============================================================

db = SQLAlchemy()
migrate = Migrate()

# ============================================================
# CREAR APLICACIÓN
# ============================================================

def create_app():

    app = Flask(__name__)

    # --------------------------------------------------------
    # CONFIGURACIÓN
    # --------------------------------------------------------

    app.config.from_object("config.Config")

    # --------------------------------------------------------
    # BASE DE DATOS
    # --------------------------------------------------------

    db.init_app(app)

    # --------------------------------------------------------
    # MIGRACIONES
    # --------------------------------------------------------

    migrate.init_app(app, db)

    # --------------------------------------------------------
    # IMPORTAR MODELOS
    # --------------------------------------------------------

    from . import models

    # --------------------------------------------------------
    # IMPORTAR BLUEPRINTS
    # --------------------------------------------------------

    from .routes import main
    from .routes_reportes import reportes

    app.register_blueprint(main)
    app.register_blueprint(reportes)

    # --------------------------------------------------------
    # CREAR TABLAS Y DATOS INICIALES
    # --------------------------------------------------------

    with app.app_context():

        db.create_all()

        from .inicializar import crear_datos_iniciales

        crear_datos_iniciales()

    return app