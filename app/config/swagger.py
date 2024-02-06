from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/api/docs'
API_URL = '/static/data/schema.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Verificador de parametros de senha"
    },
)

