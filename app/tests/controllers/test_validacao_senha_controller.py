import unittest
from unittest.mock import patch

from src.services.validador_senha import ValidadorSenha

from app import app


class TestValidacaoSenhaController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    @patch.object(ValidadorSenha, 'validar_parametros_senha')
    def test_validar_senha_retona_true_caso_senha_possua_parametros(self, mock_verifica):
        senha_valida = 'AbTp9!fok'
        expected_response = {'valida': True}

        mock_verifica.return_value = True

        response = self.app.post('/senha', json={'senha': senha_valida})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), expected_response)

    @patch.object(ValidadorSenha, 'validar_parametros_senha')
    def test_validar_senha_retona_false_caso_senha_nao_possua_parametros(self, mock_verifica):
        senha_invalida = 'AbTp9!f'
        expected_response = {'valida': False}

        mock_verifica.return_value = False

        response = self.app.post('/senha', json={'senha': senha_invalida})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), expected_response)


if __name__ == '__main__':
    unittest.main()
