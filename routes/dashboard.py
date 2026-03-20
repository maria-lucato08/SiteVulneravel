from flask import Blueprint, redirect, render_template, request, url_for
from peewee import fn 
from database.models.cards import Card_info
from database.models.users import User_info 

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/dashboard/<id>')
def dashboard(id):
    gettingUser = User_info.get_or_none(User_info.id == id)
    cards = Card_info.select().where(Card_info.holderEmail == gettingUser.email)
    
    return render_template('dashboard.html', id=gettingUser.id, name=gettingUser.name, email=gettingUser.email, cards=cards) 
    
    
@dashboard_route.route('/dashboard/new-card', methods=['POST'])
def dashboard_new_card():
    id = request.form.get('id')
    gettingUser = User_info.get_or_none(User_info.id == id)
    data = request.form # dados do formulário enviado #
    
    Card_info.create(
        holderEmail = gettingUser.email,
        numberCard = data['cardNumber'],
        holderName = data['holderName'].upper(),
        expiration = data['expiration'],
        cvv = data['cvv']
    )
    return redirect(url_for('dashboard_route.dashboard', id=gettingUser.id))

@dashboard_route.route('/dashboard/delete-card', methods=['POST'])
def dashboard_delete_card():
    id = request.form.get('id') # id do user vindo do form # 
    gettingUser = User_info.get_or_none(User_info.id == id) # verificando id para url # 
    
    last4numbers = request.form.get('card4Number') # obtendo ultimos 4 numeros do cartao a ser deletado #
    confirmLast4 = Card_info.get_or_none(fn.SUBSTR(Card_info.numberCard, -4) == last4numbers) # confirmando se esta certo os 4 numeros # 
    
    if confirmLast4 == None:
        return redirect(url_for('dashboard_route.dashboard', id=gettingUser.id))
    else:
        confirmLast4.delete_instance()
        return redirect(url_for('dashboard_route.dashboard', id=gettingUser.id))