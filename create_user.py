from getpass import getpass  #схоже с input но скрывает введенные символы
import sys  # модуль с системными функциями и вызовами

from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()  # создаем app локально, для работы с б/д в конексте создаем веб приложение???

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit(0)
    
    rols = ('admin', 'user', 'guest')
    role = input('Введите роль пользователя (admin, user, guest):')
    if role not in rols:
        print('Роль пользователя введена не верно.')
        sys.exit(0)

    password1 = getpass('Введите пароль:')
    password2 = getpass('Повторте пароль:')

    if not password1 == password2:
        print('Пароли не одинаковые')
        sys.exit(0)

    new_user = User(username=username, role=role)
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с ID {}'.format(new_user.id))

