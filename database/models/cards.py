from peewee import ForeignKeyField, Model, CharField
from database.database import db
from database.models.users import User_info

class Card_info(Model): # Define a classe Card_info que herda de Model, representando a tabela de cartões no banco de dados #
    holderEmail = ForeignKeyField(User_info, backref='cards') # Define uma chave estrangeira para a tabela de usuários, relacionando os cartões aos seus respectivos usuários #
    holderName = CharField()
    numberCard = CharField(unique=True)
    expiration = CharField(4)
    cvv = CharField(3)
    
    class Meta: # Define a classe Meta para configurar o modelo #
        database = db