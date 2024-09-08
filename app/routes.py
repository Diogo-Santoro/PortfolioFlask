
from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/sobre')
def sobre():
    return render_template('sobre.html')

@main.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        flash('Sua mensagem foi enviada com sucesso!', 'success')
        return redirect(url_for('main.contato'))
    return render_template('contato.html')
            