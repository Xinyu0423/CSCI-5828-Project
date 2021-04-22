import os
from flask import Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api


db = SQLAlchemy()
migrate = Migrate()

enable_doc = '/' if os.environ.get('FLASK_ENV') == 'development' else False
api = Api(doc=enable_doc)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


