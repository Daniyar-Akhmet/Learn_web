from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login/')
def login():
    print(current_user)
    if current_user.is_authenticated: # проверка если пользователь уже в системе то на login не выводится и преходит на главную страничку
        return redirect(url_for('news.index')) #переход на url по названию функции
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/process-login/', methods=['POST'])
def process_login():
    form = LoginForm() #создаем экземпляер, созданного нами, класса LoginForm()

    if form.validate_on_submit():  # проверка на ошибки, могут возникнуть при вводе данных пользователем в форму
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно зашли на сайт') # позволяет передавать сообщения между route-ами
            return redirect(url_for('news.index'))  # перенаправляет на другую страницу по названию ф-ции
        
    flash('Неправильно имя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout/')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('news.index'))