import os
from flask import Flask, render_template

from .config import ProductionConfig, DevelopmentConfig
from .views import api_blueprint, errors
from .extensions import db, migrate, login_manager, api
# models need to be imported before app and after db
from .models import Users, Orders, Products

def create_app(config = None):

    app = Flask(__name__)
    # Have to define index before loading flask-restx
    @app.route('/')
    def index():
        return render_template('index.html')

    if os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    register_extensions(app)
    register_blueprints(app)

    # TODO ?




    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    #api.init_app(app, doc = '/api')
    login_manager.init_app(app)

def register_blueprints(app):
    #app.register_blueprint(index)
    app.register_blueprint(errors)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from .models.users import Users     
        db.create_all()
    app.run(debug=True)