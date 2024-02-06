
class VerificadorParametrosString:
    """
       Classe possui metodos para verificar parametros de uma string
    """

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
            caracteres.add(caractere)
        return False

