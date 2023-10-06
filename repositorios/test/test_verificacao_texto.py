import unittest
from repositorios.utils.verificacao_texto import consulta_de_palavra_em_texto


class TestVerificacaoTexto(unittest.TestCase):

    def test_apenas_um_texto(self):
        texto = "Lorem ipsum dolor sit amet, PSICOLOGIA consectetur adipiscing elit. In magna."
        resultado = consulta_de_palavra_em_texto("psicologia", texto)
        self.assertEquals(resultado, True)

    def test_mais_de_um_texto(self):
        texto1 = "Lorem ipsum dolor sit amet, psicologia consectetur adipiscing elit. In magna."
        texto2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc non."
        resultado = consulta_de_palavra_em_texto("psicologia", texto1, texto2)
        self.assertEquals(resultado, True)

    def test_nao_encontra_palavra(self):
        texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ut."
        resultado = consulta_de_palavra_em_texto("psicologia", texto)
        self.assertEquals(resultado, False)
