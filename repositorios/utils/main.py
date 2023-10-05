import string
from unidecode import unidecode


def verifica(palavra_de_consulta: str, texto: str) -> bool:
    tabela_de_traducao = str.maketrans('', '', string.punctuation)
    texto_sem_pontuacao = texto.translate(tabela_de_traducao)
    texto_sem_acentos = unidecode(texto_sem_pontuacao)
    lista_palavras = texto_sem_acentos.split(" ")

    if palavra_de_consulta in lista_palavras:
        return True
    return False


def verificacao_multipla(consulta, *args):
    for texto in args:
        if verifica(consulta, texto):
            return True
    return False


if __name__ == '__main__':
    txt1 = """
    A utilização de novas técnicas de aproveitamento de resíduos 
    tem-se tornado cada vez mais importante na construção civil, 
    principalmente quando se trata da utilização de resíduos de 
    outros segmentos industriais e da redução de consumo de 
    matérias-primas naturais. O objetivo deste estudo foi avaliar 
    a utilização da lama vermelha, resíduo proveniente da produção 
    de alumina metalúrgica, na produção de blocos cerâmicos vazados 
    estruturais. A produção dos blocos foi realizada em uma indústria 
    cerâmica, a partir de uma mistura de 60% de lama vermelha (LV) e de 
    40% de argila. Após a produção dos blocos, realizaram-se ensaios
    de acordo com as normas técnicas, tais como absorção de água e 
    compressão axial simples. A partir da análise dos resultados, 
    observou-se que os blocos estruturais produzidos a partir da 
    mistura de LV sse argila atenderam aos parâmetros normativos 
    quanto ao índice de absorção de água e de resistência à compressão, 
    e que as resistências médias e características desses blocos 
    foram superiores às dos blocos cerâmicos de referência.  
    """
    txt2 = "Olha, esse é um texto de teste"
    txt3 = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed quis convallis eros. Vestibulum suscipit ex sed nibh hendrerit malesuada. 
        Ut sit amet lorem non mi rhoncus porttitor  psicologia
    """
    print(verificacao_multipla('psicologia', txt1, txt2, txt3))
