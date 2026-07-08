# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 2.0
# ARCHIVO  : inicializar.py
# MÓDULO   : Datos Iniciales del Sistema
# ============================================================

from app import db

from app.models import (
    Usuario,
    Cuenta,
    Categoria
)


# ============================================================
# CREAR DATOS INICIALES
# ============================================================

def crear_datos_iniciales():

    # ========================================================
    # USUARIO ADMINISTRADOR
    # ========================================================

    administrador = Usuario.query.filter_by(
        correo="admin@sistemafinanciero.com"
    ).first()

    if administrador is None:

        administrador = Usuario(
            nombre="Administrador",
            correo="admin@sistemafinanciero.com",
            telefono="",
            rol="ADMIN",
            activo=True
        )

        administrador.set_password("Admin123*")

        db.session.add(administrador)
        db.session.commit()

    # ========================================================
    # CUENTAS
    # ========================================================

    cuentas = [

        "Efectivo",
        "Caja",
        "Bancolombia",
        "Nequi",
        "Daviplata"

    ]

    for nombre in cuentas:

        existe = Cuenta.query.filter_by(
            nombre=nombre,
            usuario_id=administrador.id
        ).first()

        if not existe:

            db.session.add(

                Cuenta(

                    nombre=nombre,

                    usuario_id=administrador.id

                )

            )

    # ========================================================
    # CATEGORÍAS INGRESOS
    # ========================================================

    ingresos = [

        "Servicio Mecánico",
        "Venta de Repuestos",
        "Venta de Accesorios",
        "Lubricantes",
        "Otros Ingresos"

    ]

    for nombre in ingresos:

        existe = Categoria.query.filter_by(
            nombre=nombre,
            usuario_id=administrador.id
        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="INGRESO",

                    usuario_id=administrador.id

                )

            )

    # ========================================================
    # CATEGORÍAS GASTOS
    # ========================================================

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

        existe = Categoria.query.filter_by(
            nombre=nombre,
            usuario_id=administrador.id
        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="GASTO",

                    usuario_id=administrador.id

                )

            )

    # ========================================================
    # CATEGORÍAS INVERSIONES
    # ========================================================

    inversiones = [

        "Compra de Herramientas",
        "Compra de Repuestos",
        "Compra de Equipos",
        "Publicidad",
        "Capacitación"

    ]

    for nombre in inversiones:

        existe = Categoria.query.filter_by(
            nombre=nombre,
            usuario_id=administrador.id
        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="INVERSION",

                    usuario_id=administrador.id

                )

            )

    db.session.commit()