from flask import Blueprint, redirect, render_template, request, url_for
from database.models.cards import Card_info
from database.models.users import User_info 

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/dashboard')
def dashboard():
    id = request.args.get('id')
    gettingUser = User_info.get_or_none(User_info.id == id)
    
    if gettingUser == None:
        return 'Usuário não encontrado'
    else:
        return render_template('dashboard.html', name=gettingUser.name, email=gettingUser.email) 
    
@dashboard_route.route('/dashboard', methods=['POST'])
def dashboard_new_card():
    data = request.form # dados do formulário enviado #
    Card_info.create(
        holderEmail = 'admin@gmail.com',
        numberCard = data['cardNumber'],
        holderName = data['holderName'].upper(),
        expiration = data['expiration'],
        cvv = data['cvv']
    )
    return redirect(url_for('dashboard_route.dashboard'))