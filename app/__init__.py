# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 2.0
# ARCHIVO  : __init__.py
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# ============================================================
# OBJETOS GLOBALES
# ============================================================

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()

# ============================================================
# CONFIGURACIÓN LOGIN
# ============================================================

login_manager.login_view = "auth.login"

login_manager.login_message = "Debe iniciar sesión para continuar."

login_manager.login_message_category = "warning"

# ============================================================
# CARGAR USUARIO
# ============================================================

@login_manager.user_loader
def cargar_usuario(id_usuario):

    from .models import Usuario

    return Usuario.query.get(int(id_usuario))

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
    # LOGIN
    # --------------------------------------------------------

    login_manager.init_app(app)

    # --------------------------------------------------------
    # IMPORTAR MODELOS
    # --------------------------------------------------------

    from . import models

    # --------------------------------------------------------
    # BLUEPRINTS
    # --------------------------------------------------------

    from .routes import main
    from .routes_reportes import reportes
    from .auth import auth

    app.register_blueprint(main)

    app.register_blueprint(reportes)

    app.register_blueprint(auth)

    # --------------------------------------------------------
    # CREAR TABLAS
    # --------------------------------------------------------

    with app.app_context():

        db.create_all()

        from .inicializar import crear_datos_iniciales

        crear_datos_iniciales()

    return app