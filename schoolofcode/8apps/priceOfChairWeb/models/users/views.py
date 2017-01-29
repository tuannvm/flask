from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from models.users.user import User
from common.errors import UserError

userBlueprint = Blueprint('users', __name__)


@userBlueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    try:
        if User.login_valid_user(email, password):
            session['email'] = email
            return redirect(url_for(".alerts_user"))
    except UserError as e:
        return e.message
    return render_template("users/login.html")

@userBlueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    try:
        if User.register_user(email, password):
            session['email'] = email
            return redirect(url_for(".alerts_user"))
    except UserError as e:
        return e.message
    return render_template("users/register.html")

@userBlueprint.route('/alerts')
def alerts_user():
    return "this is user alert!"

@userBlueprint.route('/logout')
def logout_user():
    pass

