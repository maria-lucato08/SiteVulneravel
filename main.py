from flask import Flask
from configs import all_configs

app = Flask(__name__) # inicializando o flask; name é usado para identificar e organizar o que será executado #

all_configs(app) # passando app como parâmento #    

app.run(debug=True) # rodando o flask em modo debug para não precisar reiniciar o servidor a cada alteração #
