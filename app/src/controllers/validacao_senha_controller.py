from flask import Blueprint, request, make_response, Flask

from src.services.verificador_parametros_string import VerificadorParametrosString

senha_bp = Blueprint('/senha', __name__)


@senha_bp.route('/senha', methods=['POST'])
def confirmar_parametros_de_senha():
    body = request.json

    senha= body['senha']

    verifica_parametros = VerificadorParametrosString()
    res = verifica_parametros.validar_parametros_senha(senha)

    if res:
        response = make_response({'resposta': res}, 200)
    else:
        response = make_response({'resposta': res}, 400)

    return response
