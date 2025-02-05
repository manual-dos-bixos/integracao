from flask import Flask
from flask_migrate import Migrate
from .config import Config
from . import routes, models

# Instâncias do banco de dados e migração
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Carregar configurações
    app.config.from_object(Config)

    # Inicializar extensões
    models.db.init_app(app)
    migrate.init_app(app, models.db)

    # Registrar Blueprints
    app.register_blueprint(routes.main)

    return app
