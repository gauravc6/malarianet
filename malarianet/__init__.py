import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'notasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(db,app)

login_manager = LoginManager()
login_manager.init_app(app)

from malarianet.core.views import core
from malarianet.users.views import users
from malarianet.error_pages.handlers import error_pages
from malarianet.predict.views import predict

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(predict)
