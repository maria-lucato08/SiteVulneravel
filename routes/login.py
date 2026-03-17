from flask import Blueprint, render_template, request 
from database.database import User_info

login_route = Blueprint('login_route', __name__)

@login_route.route('/login')
def login():
    return render_template('login.html') # função que retorna algo quando a rota /login for acessada #

@login_route.route('/login', methods=['GET'])
def login_get_user():
    data = request.form # pega os dados do form #
    email = data['email']
    password = data['password']
    
    if email == User_info.email and password == User_info.password: # verifica se o email e senha correspondem aos dados do usuário #
        return render_template('dashboard.html')
    elif email != User_info.email:
        return 'email nao registrado'
    elif password != User_info.password:
        return 'senha errada'
    else:
        return 'erro'
