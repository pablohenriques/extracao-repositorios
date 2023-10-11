import scrapy


class UftSpider(scrapy.Spider):
    name = "uft"
    allowed_domains = ["repositorio.uft.edu.br"]
    start_urls = ["https://repositorio.uft.edu.br/htmlmap"]

    def parse(self, response):
        pass
