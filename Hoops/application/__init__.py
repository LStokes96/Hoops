from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('HOOPS_URI'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = getenv('KEY')

bcrypt = Bcrypt(app)

from application import routes
