from flask import Flask, render_template
from routes.signup import signup_route
from routes.login import login_route
from routes.dashboard import dashboard_route

app = Flask(__name__) # inicializando o flask; name é usado para identificar e organizar o que será executado #

app.register_blueprint(signup_route) # registrando a rota de signup #
app.register_blueprint(login_route) # registrando a rota de login #
app.register_blueprint(dashboard_route) # registrando a rota de dashboard #


app.run(debug=True) # rodando o flask em modo debug para não precisar reiniciar o servidor a cada alteração #
