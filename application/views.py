from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user


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


@views.route('/get_rooms')
def get_rooms():
    """
    :return: list of all rooms
    """
    # poki co puste
    pass
