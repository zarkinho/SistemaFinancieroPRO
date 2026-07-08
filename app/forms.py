# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 2.0
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
    StringField,
    PasswordField,
    SelectField,
    DecimalField,
    TextAreaField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError
)

from app.models import Usuario


# ============================================================
# LOGIN
# ============================================================

class LoginForm(FlaskForm):

    correo = StringField(

        "Correo",

        validators=[
            DataRequired(),
            Email()
        ]

    )

    password = PasswordField(

        "Contraseña",

        validators=[
            DataRequired()
        ]

    )

    recordar = BooleanField(

        "Recordarme"

    )

    ingresar = SubmitField(

        "Iniciar Sesión"

    )


# ============================================================
# REGISTRO
# ============================================================

class RegistroForm(FlaskForm):

    nombre = StringField(

        "Nombre Completo",

        validators=[
            DataRequired(),
            Length(max=120)
        ]

    )

    correo = StringField(

        "Correo Electrónico",

        validators=[
            DataRequired(),
            Email()
        ]

    )

    telefono = StringField(

        "Teléfono",

        validators=[
            Length(max=30)
        ]

    )

    password = PasswordField(

        "Contraseña",

        validators=[
            DataRequired(),
            Length(min=6)
        ]

    )

    confirmar = PasswordField(

        "Confirmar Contraseña",

        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Las contraseñas no coinciden."
            )
        ]

    )

    registrar = SubmitField(

        "Crear Cuenta"

    )

    # --------------------------------------------------------
    # VALIDAR CORREO
    # --------------------------------------------------------

    def validate_correo(self, correo):

        usuario = Usuario.query.filter_by(

            correo=correo.data

        ).first()

        if usuario:

            raise ValidationError(

                "Ese correo ya está registrado."
 
          )


# ============================================================
# REGISTRAR MOVIMIENTO
# ============================================================

class MovimientoForm(FlaskForm):

    tipo = SelectField(

        "Tipo de Movimiento",

        choices=[

            ("INGRESO", "Ingreso"),
            ("GASTO", "Gasto"),
            ("INVERSION", "Inversión")

        ],

        validators=[DataRequired()]

    )

    cuenta = SelectField(

        "Cuenta",

        coerce=int,

        choices=[],

        validators=[DataRequired()]

    )

    categoria = SelectField(

        "Categoría",

        coerce=int,

        choices=[],

        validators=[DataRequired()]

    )

    descripcion = StringField(

        "Descripción",

        validators=[DataRequired()]

    )

    valor = DecimalField(

        "Valor",

        places=2,

        validators=[DataRequired()]

    )

    observaciones = TextAreaField(

        "Observaciones"

    )

    guardar = SubmitField(

        "Guardar Movimiento"

    )