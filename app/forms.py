# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0 Lite
# ARCHIVO  : forms.py
# MÓDULO   : Formularios
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

from flask_wtf import FlaskForm

from wtforms import (
    SelectField,
    StringField,
    DecimalField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import DataRequired

# ============================================================
# FORMULARIO
# REGISTRAR MOVIMIENTO
# ============================================================

class MovimientoForm(FlaskForm):

    # --------------------------------------------------------
    # TIPO DE MOVIMIENTO
    # --------------------------------------------------------

    tipo = SelectField(

        "Tipo de Movimiento",

        choices=[

            ("INGRESO", "Ingreso"),

            ("GASTO", "Gasto"),

            ("INVERSION", "Inversión")

        ],

        validators=[DataRequired()]
    )

    # --------------------------------------------------------
    # CUENTA
    # --------------------------------------------------------

    cuenta = SelectField(

        "Cuenta",

        coerce=int,

        choices=[],

        validators=[DataRequired()]
    )

    # --------------------------------------------------------
    # CATEGORÍA
    # --------------------------------------------------------

    categoria = SelectField(

        "Categoría",

        coerce=int,

        choices=[],

        validators=[DataRequired()]
    )

    # --------------------------------------------------------
    # DESCRIPCIÓN
    # --------------------------------------------------------

    descripcion = StringField(

        "Descripción",

        validators=[DataRequired()]
    )

    # --------------------------------------------------------
    # VALOR
    # --------------------------------------------------------

    valor = DecimalField(

        "Valor",

        places=2,

        validators=[DataRequired()]
    )

    # --------------------------------------------------------
    # OBSERVACIONES
    # --------------------------------------------------------

    observaciones = TextAreaField(

        "Observaciones"
    )

    # --------------------------------------------------------
    # BOTÓN
    # --------------------------------------------------------

    guardar = SubmitField(

        "Guardar Movimiento"
    )