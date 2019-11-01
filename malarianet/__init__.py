import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from keras.models import load_model

app = Flask(__name__)

app.config['SECRET_KEY'] = 'notasecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users.login"

model = load_model('model.h5')
model._make_predict_function()

from malarianet.core.views import core
from malarianet.users.views import users
from malarianet.error_pages.handlers import error_pages
from malarianet.predict.views import predict

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(predict)
