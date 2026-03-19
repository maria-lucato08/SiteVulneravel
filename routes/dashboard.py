from flask import Blueprint, redirect, render_template, request, url_for
from database.models.cards import Card_info
from database.models.users import User_info 

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/dashboard/<id>')
def dashboard(id):
    gettingUser = User_info.get_or_none(User_info.id == id)
    cards = Card_info.select().where(Card_info.holderEmail == gettingUser.email)
    
    if gettingUser == None:
        return 'Usuário não encontrado'
    else:
        return render_template('dashboard.html', id=gettingUser.id, name=gettingUser.name, email=gettingUser.email, cards=cards) 
    
    
@dashboard_route.route('/dashboard', methods=['POST'])
def dashboard_new_card():
    id = request.form.get('user_id')
    print(id)
    gettingUser = User_info.get_or_none(User_info.id == id)
    data = request.form # dados do formulário enviado #
    print(gettingUser.email)
    
    Card_info.create(
        holderEmail = gettingUser.email,
        numberCard = data['cardNumber'],
        holderName = data['holderName'].upper(),
        expiration = data['expiration'],
        cvv = data['cvv']
    )
    return redirect(url_for('dashboard_route.dashboard', id=gettingUser.id))

@dashboard_route.route('/dashboard', methods=['DELETE'])
def dashboard_delete_card():
    pass