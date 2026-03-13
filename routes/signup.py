from flask import Blueprint, render_template, request

signup_route = Blueprint('signup_route', __name__)

@signup_route.route('/signup') # acessar a página #
def signup_page():
    return render_template('signup.html') # função que retorna algo quando a rota /signup for acessada #

@signup_route.route('/signup', methods=['POST']) # acessar a página com o método POST #
def signup_register():
    print(request.form) # Imprime os dados do formulário no console para verificação #
    return "Formulário de inscrição enviado com sucesso!" # Retorna uma mensagem de sucesso após o envio do formulário #