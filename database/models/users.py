from peewee import IntegerField, Model, CharField
from database.database import db

class User_info(Model): # Define a classe User_info que herda de Model, representando a tabela de usuários no banco de dados #
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    
    class Meta: # Define a classe Meta para configurar o modelo #
        database = db