from fakepinterest import db, app
from fakepinterest.models import Usuario, Post

# Exigência do contexto da aplicação para criar o banco
with app.app_context():
    db.create_all()