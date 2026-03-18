from flask import Blueprint, render_template, request
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