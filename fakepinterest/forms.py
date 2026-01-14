from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_submit_login = SubmitField('Fazer Login')
    
    # Lembrete de Renan:
    # Obrigatoriamente, o nome do método deve seguir o padrão validate_<nome_do_campo>
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário não cadastrado. Crie uma conta para continuar.')

class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome', validators=[DataRequired(), Length(min=2, max=30)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message='As senhas devem coincidir.')])
    botao_submit_criarconta = SubmitField('Criar Conta')
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Faça login para continuar.')
        
class FormPost(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_submit_post = SubmitField('Postar')