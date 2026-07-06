# ============================================================
# PROYECTO : Sistema Financiero PRO
# VERSIÓN  : 1.0
# ARCHIVO  : app.py
# MÓDULO   : Inicio del Sistema
# AUTOR    : Juan Cordero
# ASISTENTE: ChatGPT
#
# DESCRIPCIÓN:
# Este archivo inicia la aplicación Flask.
# ============================================================

# ============================================================
# IMPORTACIONES
# ============================================================

from app import create_app

# ============================================================
# CREAR APLICACIÓN
# ============================================================

app = create_app()

# ============================================================
# INICIAR SERVIDOR
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )