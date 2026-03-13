from flask import Blueprint, render_template

signup_route = Blueprint('signup_route', __name__)

@signup_route.route('/signup', methods=['GET', 'POST']) # get para acessar a página, post para enviar os dados do formulário #
def signup():
    return render_template('signup.html') # função que retorna algo quando a rota /signup for acessada #