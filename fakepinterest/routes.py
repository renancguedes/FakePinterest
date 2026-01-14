from flask import render_template, url_for, redirect
from fakepinterest import app, db, bcrypt
from fakepinterest.models import Usuario, Post
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormPost
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('login.html', form = formLogin)

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
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criarconta.html', form=formCriarConta)

@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # Usuario está acessando o próprio perfil
        formPost = FormPost()
        if formPost.validate_on_submit():
            arquivo = formPost.foto.data
            nome_seguro = secure_filename(arquivo.filename) # Garante que o nome do arquivo virá sem caracteres estranhos
            
            # Salvar o arquivo na pasta de uploads
            caminho_completo = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                        app.config['UPLOAD_FOLDER'], 
                                        nome_seguro
                                       )
            arquivo.save(caminho_completo)
            
            # Salvar o post no banco de dados
            post = Post(imagem=nome_seguro, usuario_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            
        return render_template('perfil.html', usuario=current_user, formPost=formPost)
    else:
        return render_template('perfil.html', usuario=Usuario.query.get(int(id_usuario)))
    
@app.route('/logout')
@login_required
def logout():
    logout_user() # Por padrão, essa função usa o current_user para saber quem deslogar. Então não precisa passar nada como parâmetro.
    return redirect(url_for('login'))

@app.route('/feed')
@login_required
def feed():
    posts = Post.query.order_by(Post.data_criacao.desc()).all()[:10] # Pega os 10 posts mais recentes
    return render_template('feed.html', posts=posts)