from flask import Flask, redirect, request, url_for
from configs import all_configs

app = Flask(__name__) # inicializando o flask; name é usado para identificar e organizar o que será executado #

all_configs(app) # passando app como parâmento #    

@app.route('/')
def index():
    if request.cookies.get('user_id'):
        return redirect(url_for('dashboard_route.dashboard', id=request.cookies.get('user_id'))) # redirecionando para a rota de dashboard passando o id do user vindo do cookie #
    else:
        return redirect(url_for('login_route.login')) # redirecionando para a rota de login #

app.run(host="0.0.0.0", port=5000, debug=True) # rodando o flask em modo debug para não precisar reiniciar o servidor a cada alteração #
 # redirecionando para a rota de login #