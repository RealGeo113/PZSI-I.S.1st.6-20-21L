from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from .models import db, User, Room
import json

chat = Blueprint('chat', __name__)


@chat.route('/add-room', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        roomname = request.form.get('roomname')
        password = request.form.get('password')
        roomtype = request.form.get('roomtype')
        user_limit = request.form.get('userlimit')
        accesstype = request.form.get('accesstype')
        owner_id = current_user.user_id

        room = Room.query.filter_by(roomname=roomname).first()
        if room:
            flash('Pokój o podanej nazwie już istnieje!', category='error')
        else:
            new_room = Room(roomname=roomname,
                            password=password,
                            roomtype=roomtype,
                            user_limit=user_limit,
                            accesstype=accesstype,
                            owner_id=owner_id)
            db.session.add(new_room)
            db.session.commit()

            flash('Pokój został utworzony!', category='success')

            return redirect(url_for('views.rooms'))

    return render_template("chat/add_room.html", user=current_user)


@chat.route('/delete-room', methods=['GET', 'POST'])
def delete_room():
    room = json.loads(request.data)
    room_id = room['room_id']
    room = Room.query.get(room_id)
    if room:
        if room.owner_id == current_user.user_id:
            db.session.delete(room)
            db.session.commit()

            flash('Pokój został pomyślnie usunięty.', category='success')
        else:
            flash('Nie możesz usunąć pokoju, którego nie jesteś właścicielem!', category='error')

    return jsonify({})