from app import create_app
from app.inicializar import crear_datos_iniciales

app = create_app()

with app.app_context():
    crear_datos_iniciales()

exit()