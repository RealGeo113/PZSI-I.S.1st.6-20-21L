from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user
from .models import db, User, Room, Note, UserRelation, Message
from pprint import pprint


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



@views.route('/messages', methods=['GET', 'POST'])
@login_required
def messages():
    """
    :return: list of all messages
    """
    all_messages = Message.query.all()

    return render_template("chat/history.html", user=current_user, messages=all_messages)


@views.route('/chatroom/<room_id>', methods=['GET', 'POST'])
@login_required
def chatroom(room_id):
    all_messages = Message.query.all()

    return render_template("chat/chatroom.html", user=current_user, room_id=room_id)

@views.route('/friends', methods=['GET', 'POST'])
@login_required
def friends():
    """
    :return: list of all user relations
    """
    all_relations = UserRelation.query.all()
    return render_template("friends/friends.html", user=current_user, all_relations=all_relations)

@views.route('/black-list', methods=['GET', 'POST'])
@login_required
def blocked():
    """
    :return: list of all user relations
    """
    all_relations = UserRelation.query.all()
    return render_template("friends/blocked.html", user=current_user, all_relations=all_relations)

@views.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    """
    :return: list of all users
    """

    user_list = User.query.all()

    relations = UserRelation.query.all()
    return render_template("users/users.html", user=current_user, users=user_list, relations=relations)


