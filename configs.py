from database.models.cards import Card_info
from database.models.users import User_info
from routes.signup import signup_route
from routes.login import login_route
from routes.dashboard import dashboard_route
from database.database import db

def all_configs(app):
    routes_configs(app)
    db_configs()
    app.secret_key = 'chave'

def routes_configs(app):
    app.register_blueprint(signup_route) # registrando rotas de signup #
    app.register_blueprint(login_route) # registrando rotas de login #
    app.register_blueprint(dashboard_route) # registrando rotas de dashboard #


def db_configs():
    db.connect()  # conectando ao banco de dados #
    db.create_tables([User_info])   # criando tabela #
    db.create_tables([Card_info])   # criando tabela #
