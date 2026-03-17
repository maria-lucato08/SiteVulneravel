from flask import Blueprint, render_template, request
from database.models.users import User_info

signup_route = Blueprint('signup_route', __name__)

@signup_route.route('/signup') # acessar a página #
def signup_page():
    return render_template('signup.html') # função que retorna algo quando a rota /signup for acessada #

@signup_route.route('/signup', methods=['POST']) # acessar a página com o método POST #
def signup_register():
    data = request.form # obtém os dados do formulário enviado #
    new_user = User_info.create(
        name = data['name'],
        email = data['email'],
        password = data['password']
    ) # cria novo user # 
    return 'Usuário cadastrado com sucesso!'