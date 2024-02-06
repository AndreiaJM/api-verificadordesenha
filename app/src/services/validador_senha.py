from src.services.verificador_parametros_string import VerificadorParametrosString


class ValidadorSenha:
    verificar_caracter_numerico: VerificadorParametrosString

    def __init__(self):
        self.verificar_caracter_numerico = VerificadorParametrosString()

    def validar_parametros_senha(self, senha: str) -> bool:

        """
        Metodo responsavel por validar os parametros de uma senha
        input: str
        output: boolean
        """

        if senha:

            senha = senha.replace(" ", "")

            tem_numero = self.verificar_caracter_numerico.verificar_caracter_numerico(senha)
            tamanho_minimo = self.verificar_caracter_numerico.verificar_tamanho_minimo(senha)
            tem_minusculo = self.verificar_caracter_numerico.verificar_caracter_minusculo(senha)
            tem_maiusculo = self.verificar_caracter_numerico.verificar_caracter_maiusculo(senha)
            tem_caracter_especial = self.verificar_caracter_numerico.verificar_caracter_especial(senha)
            tem_caracter_repetido = self.verificar_caracter_numerico.verificar_caracteres_repetidos(senha)

            if not tem_caracter_repetido \
                    and tem_numero \
                    and tamanho_minimo \
                    and tem_minusculo \
                    and tem_maiusculo \
                    and tem_caracter_especial:
                return True

        return False
