from flask import render_template, url_for, redirect
from fakepinterest import app, db, bcrypt
from fakepinterest.models import Usuario, Post
from flask_login import login_required, login_user, logout_user
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    return render_template('homepage.html', form = formLogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formCriarConta = FormCriarConta()
    if formCriarConta.validate_on_submit():
        # Criptografa a senha antes de salvar no banco
        senha = bcrypt.generate_password_hash(formCriarConta.senha.data).decode('utf-8')
        usuario = Usuario(nome=formCriarConta.username.data,
                          email=formCriarConta.email.data,
                          senha=senha)
        db.session.add(usuario)
        db.session.commit()
        login_user(usuario, remember=True) # O remember me mantém logado mesmo após fechar o navegador
        return redirect(url_for('perfil', usuario=usuario.nome))
    return render_template('criarconta.html', form=formCriarConta)

@app.route('/perfil/<usuario>', methods=['GET'])
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)