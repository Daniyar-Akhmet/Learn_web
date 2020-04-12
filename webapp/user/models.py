from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db

class User(db.Model, UserMixin):  # класс User наследуется от db.Model и от UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(100), index=True)
    email = db.Column(db.String(64))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property 
    def is_admin(self): # если оформлено в property то можно обращатся как свойству, а не методу (без скобочек)
        return self.role == 'admin'

    def __repr__(self):
        return '<User user={} and id={}>'.format(self.username, self.id) # при вызвове возвращает строку