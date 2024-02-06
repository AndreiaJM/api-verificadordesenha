from flask import Flask
from src.controllers.validador_senha_controller import senha_bp
from config.swagger import swaggerui_blueprint

app = Flask(__name__)

#Rotas
app.register_blueprint(senha_bp)

#Swagger
app.register_blueprint(swaggerui_blueprint)
app.static_folder = 'static'


if __name__ == '__main__':
    app.run()
