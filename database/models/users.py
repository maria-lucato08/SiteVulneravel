from peewee import Model, CharField
from database.database import db

class User_info(Model): # Define a classe User_info que herda de Model, representando a tabela de usuários no banco de dados #
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    creditsCards = CharField(default=0) # quantidade de cartões cadastrados pelo usuário, iniciando com 0 por padrão # 
    
    class Meta: # Define a classe Meta para configurar o modelo #
        database = db