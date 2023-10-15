import scrapy


class RepositoriosItem(scrapy.Item):
    url = scrapy.Field()
    tipo = scrapy.Field()
    data = scrapy.Field()
    autores = scrapy.Field()
    titulo = scrapy.Field()
    resumo = scrapy.Field()
    palavras_chave = scrapy.Field()
    repositorio = scrapy.Field()
