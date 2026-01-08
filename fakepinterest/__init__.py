from flask import Flask

app = Flask(__name__)

# Tem que ser importado depois da criação do app
from fakepinterest import routes