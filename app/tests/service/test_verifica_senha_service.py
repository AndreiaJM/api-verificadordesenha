import unittest
from unittest import TestCase
from unittest.mock import Mock

from src.services.verificador_parametros_string import VerificadorParametrosString


class TesteVerificaSenha(TestCase):
    def setUp(self):
        self.verificador_parametros = VerificadorParametrosString()

    def test_tem_parametros_retorna_true__caso_possua_todos_parametros(self):
        retorno = self.verificador_parametros.validar_parametros_senha('AbTp9!fok')

        self.assertTrue(retorno)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_numerico(self):

        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        retorno = self.verificador_parametros.validar_parametros_senha('AbTp!fok')

        self.assertFalse(retorno)

    def test_tem_parametros_retorna_false__caso_nao_possua_nove_caracteres(self):

        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.verificador_parametros.validar_parametros_senha("AbTp9")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_minusculo(self):

        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.verificador_parametros.validar_parametros_senha("ABTP9!FOK")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_maiusculo(self):

        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.verificador_parametros.validar_parametros_senha("abtp9!fok")
        self.assertFalse(resultado)

    def test_tem_parametros_retorna_false__caso_nao_possua_caracter_especial(self):

        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracteres_repetidos = Mock(return_value=False)

        resultado = self.verificador_parametros.validar_parametros_senha("AbTp9hfok")
        self.assertFalse(resultado)


    def test_tem_parametros_retorna_false__caso_possua_caracter_repetido(self):

        self.verificador_parametros.verificar_caracter_numerico = Mock(return_value=True)
        self.verificador_parametros.verificar_tamanho_minimo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_minusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_maiusculo = Mock(return_value=True)
        self.verificador_parametros.verificar_caracter_especial = Mock(return_value=True)

        resultado = self.verificador_parametros.validar_parametros_senha("AbTp9hfokkk")
        self.assertFalse(resultado)

    # ===============================================================================

    def test_verificar_numero_retorna_true__caso_pussua_caracter_numerico(self):
        retorno = self.verificador_parametros.verificar_caracter_numerico('stringcomnumero1')

        self.assertTrue(retorno)

    def test_verificar_numero_retorna_false__caso_nao_pussua_caracter_numerico(self):
        retorno = self.verificador_parametros.verificar_caracter_numerico('stringsemnumero')

        self.assertFalse(retorno)

    def test_verificar_tamanho_retorna_true__caso_pussua_nove_caracteres(self):
        retorno = self.verificador_parametros.verificar_tamanho_minimo('novecarac')

        self.assertTrue(retorno)

    def test_verificar_tamanho_retorna_false__caso_nao_pussua_nove_caracteres(self):
        retorno = self.verificador_parametros.verificar_tamanho_minimo('senha')

        self.assertFalse(retorno)

    def test_verificar_minusculo_retorna_true__caso_possua_caracterer_minusculo(self):
        retorno = self.verificador_parametros.verificar_caracter_minusculo('senha')

        self.assertTrue(retorno)

    def test_verificar_minusculo_retorna_false__caso_nao_possua_caracterer_minusculo(self):
        retorno = self.verificador_parametros.verificar_caracter_minusculo('SENHA')

        self.assertFalse(retorno)

    def test_verificar_maiusculo_retorna_true__caso_possua_caracterer_maiusculo(self):
        retorno = self.verificador_parametros.verificar_caracter_maiusculo('SEnha')

        self.assertTrue(retorno)

    def test_verificar_maiusculo_retorna_false__caso_nao_possua_caracterer_maiusculo(self):
        retorno = self.verificador_parametros.verificar_caracter_maiusculo('senha')

        self.assertFalse(retorno)

    def test_verificar_caracter_especial_retorna_true__caso_possua_caracter_especial(self):
        retorno = self.verificador_parametros.verificar_caracter_especial('senha@')

        self.assertTrue(retorno)

    def test_verificar_caracter_especial_retorna_false__caso_nao_possua_caracter_especial(self):
        retorno = self.verificador_parametros.verificar_caracter_especial('senha')

        self.assertFalse(retorno)

    def test_verificar_caracteres_repetidos_retorna_true__caso_possua_caracter_repetido(self):
        retorno = self.verificador_parametros.verificar_caracteres_repetidos('seenha')

        self.assertTrue(retorno)

    def test_verificar_caracteres_repetidos_retorna_false__caso_nao_possua_caracter_repetido(self):
        retorno = self.verificador_parametros.verificar_caracteres_repetidos('senha')

        self.assertFalse(retorno)


if __name__ == '__main__':
    unittest.main()
