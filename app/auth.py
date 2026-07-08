# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : auth.py
# MÓDULO   : Autenticación
# ============================================================

from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app import db

from app.forms import (
    LoginForm,
    RegistroForm
)

from app.models import (
    Usuario,
    Cuenta,
    Categoria
)

# ============================================================
# BLUEPRINT
# ============================================================

auth = Blueprint(
    "auth",
    __name__
)


# ============================================================
# CREAR DATOS INICIALES PARA UN USUARIO
# ============================================================

def crear_datos_usuario(usuario):

    cuentas = [
        "Efectivo",
        "Caja",
        "Bancolombia",
        "Nequi",
        "Daviplata"
    ]

    for nombre in cuentas:

        db.session.add(

            Cuenta(

                nombre=nombre,

                usuario_id=usuario.id

            )

        )

    ingresos = [

        "Servicio Mecánico",
        "Venta de Repuestos",
        "Venta de Accesorios",
        "Lubricantes",
        "Otros Ingresos"

    ]

    for nombre in ingresos:

        db.session.add(

            Categoria(

                nombre=nombre,

                tipo="INGRESO",

                usuario_id=usuario.id

            )

        )

    gastos = [

        "Mercado",
        "Transporte",
        "Combustible",
        "Internet",
        "Telefonía",
        "Agua",
        "Energía",
        "Gas",
        "Arriendo",
        "Diezmo",
        "Ofrenda",
        "Otros Gastos"

    ]

    for nombre in gastos:

        db.session.add(

            Categoria(

                nombre=nombre,

                tipo="GASTO",

                usuario_id=usuario.id

            )

        )

    inversiones = [

        "Compra de Herramientas",
        "Compra de Repuestos",
        "Compra de Equipos",
        "Publicidad",
        "Capacitación"

    ]

    for nombre in inversiones:

        db.session.add(

            Categoria(

                nombre=nombre,

                tipo="INVERSION",

                usuario_id=usuario.id

            )

        )

    db.session.commit()


# ============================================================
# LOGIN
# ============================================================

@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        return redirect(
            url_for("main.dashboard")
        )

    form = LoginForm()

    if form.validate_on_submit():

        usuario = Usuario.query.filter_by(

            correo=form.correo.data

        ).first()

        if (

            usuario

            and usuario.activo

            and usuario.check_password(

                form.password.data

            )

        ):

            login_user(

                usuario,

                remember=form.recordar.data

            )

            usuario.ultimo_acceso = datetime.utcnow()

            db.session.commit()

            flash(

                "Bienvenido.",

                "success"

            )

            return redirect(

                url_for("main.dashboard")

            )

        flash(

            "Correo o contraseña incorrectos.",

            "danger"

        )

    return render_template(

        "login.html",

        form=form

    )


# ============================================================
# REGISTRO
# ============================================================

@auth.route("/registro", methods=["GET", "POST"])
def registro():

    form = RegistroForm()

    if form.validate_on_submit():

        usuario = Usuario(

            nombre=form.nombre.data,

            correo=form.correo.data,

            telefono=form.telefono.data

        )

        usuario.set_password(

            form.password.data

        )

        db.session.add(

            usuario

        )

        db.session.commit()

        crear_datos_usuario(usuario)

        flash(

            "Usuario creado correctamente.",

            "success"

        )

        return redirect(

            url_for("auth.login")

        )

    return render_template(

        "registro.html",

        form=form

    )


# ============================================================
# LOGOUT
# ============================================================

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(

        "Sesión finalizada.",

        "info"

    )

    return redirect(

        url_for("auth.login")

    )