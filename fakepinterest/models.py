from fakepinterest import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(usuario_id):
    return Usuario.query.get(int(usuario_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='usuario', lazy=True)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagem = db.Column(db.String, default='default.png')
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.imagem} by Usuario ID {self.usuario_id}>'