# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0
# ARCHIVO  : models.py
# MÓDULO   : Base de Datos
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
#
# DESCRIPCIÓN:
# Este archivo contiene todos los modelos (tablas)
# principales de la base de datos.
#
# TABLAS:
#   ✓ Cuenta
#   ✓ Categoria
#   ✓ Movimiento
# ============================================================


# ============================================================
# IMPORTACIONES
# ============================================================

from datetime import datetime

from flask_login import UserMixin

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app import db


# ============================================================
# TABLA: CUENTAS
# ============================================================
#
# Guarda todas las cuentas financieras.
#
# Ejemplos:
#
# • Caja
# • Bancolombia
# • Nequi
# • Daviplata
#
# ============================================================

class Cuenta(db.Model):

    __tablename__ = "cuentas"

    # --------------------------------------------------------
    # Llave primaria
    # --------------------------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # --------------------------------------------------------
    # Nombre de la cuenta
    # --------------------------------------------------------

    nombre = db.Column(
        db.String(100),
        nullable=True
    )

    # --------------------------------------------------------
    # Saldo inicial
    # --------------------------------------------------------

    saldo_inicial = db.Column(
        db.Numeric(12, 2),
        default=0
    )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    activa = db.Column(
        db.Boolean,
        default=True
    )

    # --------------------------------------------------------
    # Fecha de creación
    # --------------------------------------------------------

    fecha_creacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # --------------------------------------------------------
    # USUARIO PROPIETARIO
    # --------------------------------------------------------

    usuario_id = db.Column(
       db.Integer,
       db.ForeignKey("usuarios.id"),
       nullable=True
    )

    # --------------------------------------------------------
    # Relación con Movimientos
    # --------------------------------------------------------

    movimientos = db.relationship(
        "Movimiento",
        backref="cuenta",
        lazy=True
    )

    # --------------------------------------------------------
    # Representación del objeto
    # --------------------------------------------------------

    def __repr__(self):
        return f"<Cuenta {self.nombre}>"


# ============================================================
# TABLA: CATEGORIAS
# ============================================================
#
# Almacena todas las categorías disponibles.
#
# INGRESOS
# • Servicio Mecánico
# • Venta de Repuestos
#
# INVERSIONES
# • Compra de Repuestos
# • Herramientas
#
# GASTOS
# • Mercado
# • Transporte
# • Internet
# • Energía
# • Diezmo
# • Ofrenda
#
# ============================================================

class Categoria(db.Model):

    __tablename__ = "categorias"

    # --------------------------------------------------------
    # Llave primaria
    # --------------------------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # --------------------------------------------------------
    # Nombre
    # --------------------------------------------------------

    nombre = db.Column(
        db.String(100),
        nullable=True
    )

    # --------------------------------------------------------
    # Tipo
    #
    # INGRESO
    # GASTO
    # INVERSION
    # TRANSFERENCIA
    # --------------------------------------------------------

    tipo = db.Column(
        db.String(20),
        nullable=True
    )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    activa = db.Column(
        db.Boolean,
        default=True
    )

    # --------------------------------------------------------
    # USUARIO PROPIETARIO
    # --------------------------------------------------------

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=True
    )

    # --------------------------------------------------------
    # Relación con Movimientos
    # --------------------------------------------------------

    movimientos = db.relationship(
        "Movimiento",
        backref="categoria",
        lazy=True
    )

    # --------------------------------------------------------
    # Representación del objeto
    # --------------------------------------------------------

    def __repr__(self):
        return f"<Categoria {self.nombre}>"


# ============================================================
# TABLA: MOVIMIENTOS
# ============================================================
#
# Esta es la tabla más importante del sistema.
#
# Aquí se registran:
#
# ✓ Ingresos
# ✓ Gastos
# ✓ Inversiones
# ✓ Transferencias
#
# A partir de esta información se generarán:
#
# ✓ Reporte Diario
# ✓ Semanal
# ✓ Quincenal
# ✓ Mensual
# ✓ Trimestral
# ✓ Semestral
# ✓ Anual
# ✓ Personalizado
#
# ============================================================

class Movimiento(db.Model):

    __tablename__ = "movimientos"

    # --------------------------------------------------------
    # Llave primaria
    # --------------------------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # --------------------------------------------------------
    # Fecha del movimiento
    # --------------------------------------------------------

    fecha = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # --------------------------------------------------------
    # Fecha en que el registro fue creado
    # --------------------------------------------------------

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # --------------------------------------------------------
    # Tipo
    # --------------------------------------------------------

    tipo = db.Column(
        db.String(20),
        nullable=False
    )

    # --------------------------------------------------------
    # Descripción
    # --------------------------------------------------------

    descripcion = db.Column(
        db.String(300),
        nullable=False
    )

    # --------------------------------------------------------
    # Valor
    # --------------------------------------------------------

    valor = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    # --------------------------------------------------------
    # Número de comprobante
    # --------------------------------------------------------

    numero_comprobante = db.Column(
        db.String(50)
    )

    # --------------------------------------------------------
    # Observaciones
    # --------------------------------------------------------

    observaciones = db.Column(
        db.Text
    )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    activo = db.Column(
        db.Boolean,
        default=True
    )

    # --------------------------------------------------------
    # Cuenta relacionada
    # --------------------------------------------------------

    cuenta_id = db.Column(
        db.Integer,
        db.ForeignKey("cuentas.id"),
        nullable=False
    )

    # --------------------------------------------------------
    # Categoría relacionada
    # --------------------------------------------------------

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey("categorias.id"),
        nullable=False
    )

    # --------------------------------------------------------
    # USUARIO PROPIETARIO
    # --------------------------------------------------------

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=True
    )

    # --------------------------------------------------------
    # Representación del objeto
    # --------------------------------------------------------

    def __repr__(self):
        return f"<Movimiento {self.id}>"

# ============================================================
# FIN DEL ARCHIVO
# ============================================================

# ============================================================
# PRESUPUESTO
# ============================================================

class Presupuesto(db.Model):

    __tablename__ = "presupuestos"

    id = db.Column(

        db.Integer,

        primary_key=True

    )

    categoria_id = db.Column(

        db.Integer,

        db.ForeignKey(

            "categorias.id"

        ),

        nullable=True

    )

    valor_presupuestado = db.Column(

        db.Float,

        nullable=True

    )

    mes = db.Column(

        db.Integer,

        nullable=True

    )

    anio = db.Column(

        db.Integer,

        nullable=True

    )

    categoria = db.relationship(

        "Categoria"

    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=True
   )
    

# ============================================================
# CONFIGURACIÓN DEL SISTEMA
# ============================================================

class Configuracion(db.Model):

    __tablename__ = "configuracion"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre_empresa = db.Column(
        db.String(150),
        default=""
    )

    propietario = db.Column(
        db.String(150),
        default=""
    )

    telefono = db.Column(
        db.String(50),
        default=""
    )

    correo = db.Column(
        db.String(120),
        default=""
    )

    direccion = db.Column(
        db.String(200),
        default=""
    )

    ciudad = db.Column(
        db.String(100),
        default=""
    )

    moneda = db.Column(
        db.String(20),
        default="$"
    )

    color_principal = db.Column(
        db.String(20),
        default="#0d6efd"
    )

    color_secundario = db.Column(
        db.String(20),
        default="#198754"
    )

    logo = db.Column(
        db.String(250),
        nullable=True
    )

    fecha_actualizacion = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # --------------------------------------------------------
    # USUARIO PROPIETARIO
    # --------------------------------------------------------

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False,
        unique=True
    )

    usuario = db.relationship(
        "Usuario",
        backref=db.backref(
            "configuracion",
            uselist=False
        )
    )

    def __repr__(self):
        return "<Configuracion>"
    
    # ============================================================
# TABLA: USUARIOS
# ============================================================

class Usuario(UserMixin, db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(120),
        nullable=False
    )

    correo = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    telefono = db.Column(
        db.String(30)
    )

    foto = db.Column(
        db.String(250),
        default="default.png"
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    rol = db.Column(
        db.String(20),
        default="USUARIO"
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    ultimo_acceso = db.Column(
        db.DateTime
    )

    # --------------------------------------------------------
    # MÉTODOS
    # --------------------------------------------------------

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(
            self.password_hash,
            password
        )

    def __repr__(self):

        return f"<Usuario {self.correo}>"
    
    # ============================================================
    # RELACIONES
    # ============================================================

    cuentas = db.relationship(

        "Cuenta",

        backref="usuario",

        lazy=True,

        cascade="all, delete-orphan"

    )

    categorias = db.relationship(

        "Categoria",

        backref="usuario",

        lazy=True,

        cascade="all, delete-orphan"

    )

    movimientos = db.relationship(

        "Movimiento",

        backref="usuario",

        lazy=True,

        cascade="all, delete-orphan"

    )

    presupuestos = db.relationship(

        "Presupuesto",

        backref="usuario",

        lazy=True,

        cascade="all, delete-orphan"

    )