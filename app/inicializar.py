# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : inicializar.py
# ============================================================

from app import db
from app.models import Cuenta
from app.models import Categoria


def crear_datos_iniciales():

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

            nombre=nombre

        ).first()

        if not existe:

            db.session.add(

                Cuenta(

                    nombre=nombre

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

            nombre=nombre

        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="INGRESO"

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

            nombre=nombre

        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="GASTO"

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

            nombre=nombre

        ).first()

        if not existe:

            db.session.add(

                Categoria(

                    nombre=nombre,

                    tipo="INVERSION"

                )

            )

    db.session.commit()