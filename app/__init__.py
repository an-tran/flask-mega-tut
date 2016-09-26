import os

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy
from config import baseDir

app = Flask(__name__)
app.config.from_object('app.config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(baseDir, 'tmp'))

from app import views, models
