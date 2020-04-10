from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_required

from webapp.db import db
from webapp.user.models import User
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.weather import weather_by_city


def create_app(): # "фабрика" - функция которая создает Flask app, инициализирует его и возвращает app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager() #создаем экземпляр LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'  # 'user.login' название ф-ции которая занимается логином пользователя
    
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    # проверяем пользователя
    @login_manager.user_loader #login_manager вытаскивает из сессионой cookie user_id 
    def load_user(user_id): # пeредает user_id в load_user
        return User.query.get(user_id) # запрашиваем из б/д

    
    return app