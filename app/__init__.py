import os
from flask import Flask
from dotenv import load_dotenv
from app.database.models import db
from app.routes.web_routes import web_bp

# Carga las variables de tu archivo .env (donde está la conexión a SQL Server)
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # 1. Configuración de la Base de Datos y Seguridad
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'clave_respaldo_segura')

    # 2. Inicializar SQLAlchemy con la app
    db.init_app(app)

    # 3. Crear las carpetas físicas si no existen (¡Muy importante para evitar errores al subir fotos!)
    os.makedirs('app/static/uploads', exist_ok=True)

    # 4. Registrar los Blueprints (Las rutas de tu API)
    # Importamos las rutas desde la carpeta routes
    from app.routes.base_routes import base_bp
    from app.routes.reporte_routes import reporte_bp
    app.register_blueprint(web_bp)
    
    # Le decimos a Flask que las active
    app.register_blueprint(base_bp)
    app.register_blueprint(reporte_bp)

    # 5. Sincronizar con SQL Server (DBeaver)
    with app.app_context():
        # Este comando lee tus models.py y crea las 5 tablas en la base de datos
        # Si las tablas ya existen, simplemente las ignora sin borrar tus datos.
        db.create_all()

    return app