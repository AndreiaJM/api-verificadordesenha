from flask import Flask

from src.controllers.validacao_senha_controller import senha_bp

app = Flask(__name__)

app.register_blueprint(senha_bp)

if __name__ == '__main__':
    app.run()
