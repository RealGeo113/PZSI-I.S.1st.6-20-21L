from os import path
from flask import Flask
from flask_login import LoginManager
from .models import db


# inicjalizacja flaska
def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.DevConfig')
    app.config.from_object('config.ProdConfig')

    db.init_app(app)
    
    # konfiguracja routes
    # dajemy znac programowi ze te moduly istnieja
    from .views import views
    from .auth import auth
    from .chat import chat
    from .notes import notes
    from .models import User
    from .users import users
    from .friends import friends

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(chat, url_prefix='/')
    app.register_blueprint(notes, url_prefix='/')
    app.register_blueprint(users, url_prefix='/')
    app.register_blueprint(friends, url_prefix='/')
    # zaimportuj modele z bazy danych
    # jesli jeszcze nie ma stworzonej bazy danych, to ja utworz
    # ale tylko w przypadku przyjecia konfiguracji Dev
    if app.config['FLASK_ENV'] == 'development':
        create_dev_database(app)

    # deklaracja obiektu typu LoginManager
    # zmieniamy mu potem zmienne zeby przekierowywal uzytkownikow na odpowiednie strony
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_dev_database(app):
    if not path.exists('application/' + app.config['DEV_DB_NAME']):
        db.create_all(app=app)
        print('Baza danych została utworzona.')
