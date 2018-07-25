from flask import current_app
from app.extensions import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    # 头像
    icon = db.Column(db.String(64), default='default.jpeg')

    @property
    def password(self):
        raise AttributeError('不能访问密码属性')

    @password.setter
    def password(self, password):
        # 密码需要加密后存储
        self.password_hash = generate_password_hash(password)

    # 校验密码
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 生成账户激活的token
    def generate_activate_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id})

    # 校验账户激活的token
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        u = User.query.get(data['id'])
        if not u:
            return False
        if not u.confirmed:
            u.confirmed = True
            db.session.add(u)
        return True


# 该装饰器其实就是一个回调函数
@login_manager.user_loader
def loader_user(uid):
    return User.query.get(uid)
