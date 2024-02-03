
class VerificadorParametrosString:

    def validar_parametros_senha(self, senha: str):

        if senha:

            senha = senha.replace(" ", "")

            tem_numero = self.verificar_caracter_numerico(senha)
            tamanho_minimo = self.verificar_tamanho_minimo(senha)
            tem_minusculo = self.verificar_caracter_minusculo(senha)
            tem_maiusculo = self.verificar_caracter_maiusculo(senha)
            tem_caracter_especial = self.verificar_caracter_especial(senha)
            tem_caracter_repetido = self.verificar_caracteres_repetidos(senha)

            if not tem_caracter_repetido \
                    and tem_numero \
                    and tamanho_minimo \
                    and tem_minusculo \
                    and tem_maiusculo \
                    and tem_caracter_especial:
                return True

        return False

    def verificar_caracter_numerico(self, senha: str) -> bool:
        for caractere in senha:
            if caractere.isdigit():
                return True
        return False

    def verificar_tamanho_minimo(self, senha: str) -> bool:
        if len(senha) >= 9:
            return True
        else:
            return False

    def verificar_caracter_minusculo(self, senha: str) -> bool:
        for caractere in senha:
            if caractere.islower():
                return True
        return False

    def verificar_caracter_maiusculo(self, senha: str) -> bool:
        for caractere in senha:
            if caractere.isupper():
                return True
        return False

    def verificar_caracter_especial(self, senha: str) -> bool:
        caracteres_especiais = "!@#$%^&*()-+"
        for caractere in senha:
            if caractere in caracteres_especiais:
                return True
        return False

    def verificar_caracteres_repetidos(self, texto):
        caracteres = set()
        for caractere in texto:
            if caractere in caracteres:
                return True
            caracteres.add(caractere) #caso tenha caracter numerico retorna true
        return False


if __name__ == '__main__':
    c = VerificadorParametrosString()
    r = c.tem_parametros('AbTp9!fok')
    print(r)
