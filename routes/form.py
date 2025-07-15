from flask import Blueprint, render_template, redirect, url_for, flash
from models import UsuarioForm, Usuario, Notas, db, mail
from flask_mail import Message

form_route = Blueprint('form', __name__, url_prefix='/form')

@form_route.route('/', methods=['GET', 'POST'])
def form():
    form = UsuarioForm()

    if form.validate_on_submit():
        return redirect(url_for('form.form'))

    return render_template('form.html', form=form)

@form_route.route('/enviar-mensagem', methods=['POST'])
def enviar_mensagem():
    form = UsuarioForm()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data.strip().lower()
        nota = form.nota.data

        usuario_existente = Usuario.query.filter_by(email=email).first()
        if not usuario_existente:
            dados_usuario = Usuario(nome=nome, email=email)
            db.session.add(dados_usuario)
            db.session.commit()
        
            nota_usuario = Notas(nota=nota, usuario_id=dados_usuario.id)
            db.session.add(nota_usuario)
            db.session.commit()

            msg = Message(
                subject='Nova mensagem recebida!',
                recipients=['caio.dev.araujo@gmail.com'],
                body=f'Nome: {nome}\nE-mail: {email}\nNota:\n{nota}'
            )

            mail.send(msg)
        else:
            nota_usuario = Notas(nota=nota, usuario_id = usuario_existente.id)
            db.session.add(nota_usuario)
            db.session.commit()

        flash('Mensagem enviada com sucesso!')
        return redirect(url_for('form.form'))  
    
    return render_template('form.html', form=form)