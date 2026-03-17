from flask import Blueprint, render_template, request 
from database.models.users import User_info

login_route = Blueprint('login_route', __name__)

@login_route.route('/login')
def login():
    return render_template('login.html') # função que retorna algo quando a rota /login for acessada #

@login_route.route('/login')
def login_get_user():
    user_email = request.form['email'] # obtém o email do formulário enviado #
    user_password = request.form['password'] # obtém a senha do formulário enviado #
    if user_email == User_info.email and user_password == User_info.password: # verifica se o email e senha correspondem aos dados do usuário #
        