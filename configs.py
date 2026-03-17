from routes.signup import signup_route
from routes.login import login_route
from routes.dashboard import dashboard_route
from database.database import db
from database.models.users import User_info

def all_configs(app):
    routes_configs(app)
    db_configs()

def routes_configs(app):
    app.register_blueprint(signup_route) # registrando a rota de signup #
    app.register_blueprint(login_route) # registrando a rota de login #
    app.register_blueprint(dashboard_route) # registrando a rota de dashboard #


def db_configs():
    db.connect()  # conectando ao banco de dados #
    db.create_tables([User_info])   # criando tabela #
