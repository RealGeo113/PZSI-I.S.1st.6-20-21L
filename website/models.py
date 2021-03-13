# importujemy z __init__.py objekt o nazwie db
# czyli 'uchwyt' do bazy danych
# UserMixin to modul ulatwiajacy napisanie logowania
# tworzymy tutaj modele na wzor naszych tabel w bazie danych

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # zdefiniowanie klucza obcego
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# klasa uzytkownik musi dziedziczyc po db.Model oraz UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))

    # zarejestrowanie zwiazku z inna tabela
    notes = db.relationship('Note')