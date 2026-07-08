# ============================================================
# PROYECTO : Sistema Financiero PRO
# ARCHIVO  : reportes_pdf.py
# VERSIÓN  : 2.0 MULTIUSUARIO
# ============================================================

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from flask import send_file

from app.models import Movimiento


# ============================================================
# GENERAR PDF
# ============================================================

def generar_pdf(usuario_id):

    buffer = BytesIO()

    documento = SimpleDocTemplate(

        buffer,

        pagesize=letter

    )

    datos = [[

        "Fecha",

        "Tipo",

        "Cuenta",

        "Categoría",

        "Valor"

    ]]

    movimientos = (

        Movimiento.query

        .filter_by(

            usuario_id=usuario_id

        )

        .order_by(

            Movimiento.fecha.desc()

        )

        .all()

    )

    for movimiento in movimientos:

        datos.append([

            movimiento.fecha.strftime("%d/%m/%Y"),

            movimiento.tipo,

            movimiento.cuenta.nombre,

            movimiento.categoria.nombre,

            f"${movimiento.valor:,.0f}"

        ])

    tabla = Table(datos)

    tabla.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.grey),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)

        ])

    )

    documento.build(

        [tabla]

    )

    buffer.seek(0)

    return send_file(

        buffer,

        as_attachment=True,

        download_name="Reporte_Financiero.pdf",

        mimetype="application/pdf"

    )