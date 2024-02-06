import unittest
from unittest.mock import Mock

from src.services.validador_senha import ValidadorSenha
from src.services.verificador_parametros_string import VerificadorParametrosString


class TestValidadorSenha(unittest.TestCase):
    verificador_parametros: VerificadorParametrosString
    validador_senha: ValidadorSenha

    def setUp(self):
        self.verificador_parametros = VerificadorParametrosString()
        self.validador_senha = ValidadorSenha()
        ...

    def test_tem_parametros_retorna_true__caso_possua_todos_parametros(self):
        retorno = self.validador_senha.validar_parametros_senha('AbTp9!fok')

        self.assertTrue(retorno)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_numerico(self):
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        retorno = self.validador_senha.validar_parametros_senha('AbTp!fok')

        self.assertFalse(retorno)

    def test_tem_parametros_retorna_false__caso_nao_possua_nove_caracteres(self):
        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.validador_senha.validar_parametros_senha("AbTp9")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_minusculo(self):
        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.validador_senha.validar_parametros_senha("ABTP9!FOK")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_maiusculo(self):
        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.validador_senha.validar_parametros_senha("abtp9!fok")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_especial(self):
        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.validador_senha.validar_parametros_senha("AbTp9hfok")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_possua_caracter_repetido(self):
        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)

        resultado = self.validador_senha.validar_parametros_senha("AbTp9hfokkk")
        self.assertFalse(resultado)
