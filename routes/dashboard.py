from flask import Blueprint, render_template 

dashboard_route = Blueprint('dashboard_route', __name__)

@dashboard_route.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') # função que retorna algo quando a rota /dashboard for acessada #