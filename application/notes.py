from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from .models import db, Note
import json

notes = Blueprint('notes', __name__)


@notes.route('/add-note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        content = request.form.get('roomname')
        owner_id = current_user.user_id

        new_note = Note(content=content, owner_id=owner_id)

        db.session.add(new_note)
        db.session.commit()

        flash('Notatka została dodana', category='success')

    return render_template("notes/notes.html", user=current_user)


@notes.route('/edit-note', methods=['GET', 'POST'])
def edit_note():
    note = json.loads(request.data)
    note_id = note['note_id']
    note = Note.query.get(note_id)
    if note:
        if note.owner_id == current_user.user_id:
            return render_template("notes/add_note.html", user=current_user, note=note)
    else:
        flash('Błąd podczas próby edycji notatki', category='failure')
        return


@notes.route('/delete-note', methods=['GET', 'POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['note_id']
    note = Note.query.get(note_id)
    if note:
        if note.owner_id == current_user.user_id:
            db.session.delete(note)
            db.session.commit()

            flash('Notatka została pomyślnie usunięta.', category='success')

    return jsonify({})