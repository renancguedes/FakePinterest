from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Configuração do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# A secret key está aqui apenas como lembrete. Sei que não é seguro deixá-la exposta aqui.
app.config["SECRET_KEY"] = "719fd842589c207174e91e4d3bde6ebc"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

# Tem que ser importado depois da criação do app
from fakepinterest import models
from fakepinterest import routes