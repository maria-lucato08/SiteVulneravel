from flask import Blueprint, redirect, render_template, request, url_for, flash
from database.models.users import User_info

login_route = Blueprint('login_route', __name__)

@login_route.route('/login')
def login():
    return render_template('login.html') # função que retorna algo quando a rota /login for acessada #

@login_route.route('/login/get-user', methods=['GET'])
def login_get_user():
    # por meio dos argumentos da url #
    email = request.args.get('email') 
    password = request.args.get('password')
    
    userVetification = User_info.get_or_none(User_info.email == email) # se existir retorma o valor, se não retorna none #
   
    if userVetification == None:
        flash('Usuário não encontrado')
        return redirect(url_for('login_route.login'))
    elif userVetification.password != password:
        flash('Senha incorreta')
        return redirect(url_for('login_route.login'))
    else:
        return redirect(url_for('dashboard_route.dashboard', id=userVetification.id))
