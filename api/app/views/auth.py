from flask import redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from flask_restx import Api, Resource, Namespace

from ..extensions import db
from ..models import Users
from .forms import LoginForm

api = Namespace('auth',path='/')

@api.route('/login')
class Login(Resource):
    @api.doc("Login")
    def post(self):
        email = request.form.get('email')
        password = request.form.get('pwd')
        remember = True

        user = Users.query.filter_by(email=email).first()

        if not user or not user.password==password:
            flash('Wrong password')
            return "Wrong username or password"
        login_user(user, remember = remember)
        
        return "Login successful"


@api.route('/register')
class Register(Resource):
    @api.doc("Register")
    def post(self):
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        
        if user:
            return "User Already exists."
        new_user = Users(email=email, firstname=firstname, lastname=lastname, password=password)
        models.db.session.add(new_user)
        models.db.session.commit()

        return redirect(url_for('auth.login'))


@api.route('/logout')
class Logout(Resource):
    @api.doc("Logout")
    @login_required
    def get():
        logout_user()
        return "loged out."
