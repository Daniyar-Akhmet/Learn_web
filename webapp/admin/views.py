from flask_login import current_user, login_required
from flask import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@login_required  #проверка если не авторизован то перебрасывает на login
def admin_index():
    if current_user.is_admin:
        return 'Привет админ'
    else:
        return 'Привет ты не админ'
