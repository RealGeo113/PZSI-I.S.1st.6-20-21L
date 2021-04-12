from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from .models import db, User, Room, Note


# tutaj sa tworzone Routes - czyli podstrony na ktore serwer ma kierowac zapytanie
views = Blueprint('views', __name__)


# zabezpieczenie przed wyswietlaniem strony domowej jesli uzytkownik nie jest zalogowany
# za pomoca login_required
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # za kazdym razem bedzie renderowana strona home.html
    # ktora korzysta z base.html
    # jedynie zmienia bloki w base.html na swoje
    # jest to duze ulatwienie i oszczednosc czasu
    return render_template("home.html", user=current_user)


@views.route('/rooms', methods=['GET', 'POST'])
@login_required
def rooms():
    """
    :return: list of all rooms
    """
    all_rooms = Room.query.all()
    # print(all_rooms)

    return render_template("chat/rooms.html", user=current_user, all_rooms=all_rooms)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    """
    :return: list of all notes
    """
    all_notes = Note.query.all()

    return render_template("notes/notes.html", user=current_user, all_notes=all_notes)
