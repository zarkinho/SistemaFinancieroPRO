# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : routes_reportes.py
# MÓDULO   : Reportes
# ============================================================

from datetime import datetime

from flask import Blueprint
from flask import render_template
from flask import request

from sqlalchemy import func

from app import db

from app.models import Movimiento

reportes = Blueprint(
    "reportes",
    __name__
)


# ============================================================
# REPORTES
# ============================================================

@reportes.route("/reportes")
def reporte_general():

    inicio = request.args.get("inicio")
    fin = request.args.get("fin")

    consulta = Movimiento.query

    if inicio:

        fecha_inicio = datetime.strptime(
            inicio,
            "%Y-%m-%d"
        )

        consulta = consulta.filter(
            Movimiento.fecha >= fecha_inicio
        )

    if fin:

        fecha_fin = datetime.strptime(
            fin,
            "%Y-%m-%d"
        )

        fecha_fin = fecha_fin.replace(
            hour=23,
            minute=59,
            second=59
        )

        consulta = consulta.filter(
            Movimiento.fecha <= fecha_fin
        )

    movimientos = consulta.order_by(
        Movimiento.fecha.desc()
    ).all()

    ingresos = sum(
        m.valor
        for m in movimientos
        if m.tipo == "INGRESO"
    )

    gastos = sum(
        m.valor
        for m in movimientos
        if m.tipo == "GASTO"
    )

    inversiones = sum(
        m.valor
        for m in movimientos
        if m.tipo == "INVERSION"
    )

    saldo = ingresos - gastos - inversiones

    return render_template(

        "reportes.html",

        movimientos=movimientos,

        ingresos=ingresos,

        gastos=gastos,

        inversiones=inversiones,

        saldo=saldo,

        inicio=inicio,

        fin=fin

    )