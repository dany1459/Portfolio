from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Message
    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('database created!')

# def create_app():
#     app = Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#     api = Api(app)
#     db.init_app(app) # initialize the database
#     db.create_all(app=app) # create tables
#     api.add_resource(HomeRoute, '/')
#     api.add_resource(HomeRouteWithId, '/<string:id>')
#     return app