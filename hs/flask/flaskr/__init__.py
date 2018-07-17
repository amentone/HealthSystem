from flask import Flask, request, render_template, Blueprint
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_required
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRETKEY')

app.config['MONGO_DBNAME'] = 'healthsystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbahealthsystem:passwddba@postgres:5432/healthsystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER']= os.environ.get('MAIL_USERNAME')

mail = Mail(app)
mongo = PyMongo(app, "mongodb://dbahealthsystem:passwddba@mongo:27017/healthsystem")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from .sql import models
from . import error_handler
from . import views

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
