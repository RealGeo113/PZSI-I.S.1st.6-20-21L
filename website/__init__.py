from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# inicjalizacja flaska
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tajnyklucztajnyklucz'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # konfiguracja routes
    # dajemy znac programowi ze te moduly istnieja
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # zaimportuj modele z bazy danych
    # jesli jeszcze nie ma stworzonej bazy danych, to ja utworz
    from .models import User, Note

    create_database(app)

    # deklaracja obiektu typu LoginManager
    # zmieniamy mu potem zmienne zeby przekierowywal uzytnikow na odpowiednie strony
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Baza danych została utworzona.')