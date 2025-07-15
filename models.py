# Bibliotecas SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Biblioteca Flask-Mail
from flask_mail import Mail

# Bibliotecas Flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

db = SQLAlchemy()
mail = Mail()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False, unique = True)
    nota = db.relationship('Notas', backref='usuario', lazy=True)

class Notas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    nota = db.Column(db.String(10000), nullable = False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

class UsuarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='O nome precisa ser preenchido.')])
    email = StringField('E-mail', validators=[DataRequired(message='O email não pode ser um campo vazio.'), Email(message='Preencha com um e-mail válido.')])
    nota = TextAreaField('Nota', validators=[DataRequired(message='Escreva algo na nota.')])
    enviar = SubmitField('Enviar')