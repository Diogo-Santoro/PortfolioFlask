from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sua_chave_secreta_aqui'  # Assegure-se de que a chave secreta está definida

    from .routes import main
    app.register_blueprint(main)

    return app
