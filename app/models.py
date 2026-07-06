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
        nullable=False
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
        nullable=False
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
        nullable=False
    )

    # --------------------------------------------------------
    # Estado
    # --------------------------------------------------------

    activa = db.Column(
        db.Boolean,
        default=True
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

        nullable=False

    )

    valor_presupuestado = db.Column(

        db.Float,

        nullable=False

    )

    mes = db.Column(

        db.Integer,

        nullable=False

    )

    anio = db.Column(

        db.Integer,

        nullable=False

    )

    categoria = db.relationship(

        "Categoria"

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

    def __repr__(self):
        return "<Configuracion>"