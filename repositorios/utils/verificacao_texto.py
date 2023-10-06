import string
from unidecode import unidecode


def verificacao(palavra_de_consulta: str, texto: str) -> bool:
    tabela_de_traducao = str.maketrans('', '', string.punctuation)
    texto_sem_pontuacao = texto.translate(tabela_de_traducao)
    texto_sem_acentos = unidecode(texto_sem_pontuacao.lower())
    texto_sem_quebras_linha = texto_sem_acentos.replace('\n', ' ')
    lista_palavras = texto_sem_quebras_linha.split(" ")

    if palavra_de_consulta in lista_palavras:
        return True
    return False


def consulta_de_palavra_em_texto(consulta, *args):
    for texto in args:
        if verificacao(consulta, texto):
            return True
    return False
