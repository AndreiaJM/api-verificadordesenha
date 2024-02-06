from flask import Blueprint, request, make_response

from src.services.validador_senha import ValidadorSenha

senha_bp = Blueprint('api', __name__)


@senha_bp.route('/senha', methods=['POST'])
def validar_senha():
    try:

        body = request.json
        senha = body['senha']

        verifica_parametros = ValidadorSenha()
        res = verifica_parametros.validar_parametros_senha(senha)

        if res:
            response = make_response({'valida': res}, 200)
        else:
            response = make_response({'valida': res}, 400)

        return response

    except Exception as e:
        response = make_response({'error': 'Ocorreu um erro ao validar a senha'}, 500)
        return response
