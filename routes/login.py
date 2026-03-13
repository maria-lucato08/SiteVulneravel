from flask import Blueprint, render_template 

login_route = Blueprint('login_route', __name__)

@login_route.route('/login')
def login():
    return render_template('login.html') # função que retorna algo quando a rota /login for acessada #