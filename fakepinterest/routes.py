from flask import render_template, url_for
from fakepinterest import app

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/perfil/<usuario>', methods=['GET'])
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)