import scrapy

from repositorios.items import RepositoriosItem
from utils.verificacao_texto import consulta_de_palavra_em_texto


class UfpaSpider(scrapy.Spider):
    name = "ufpa"
    allowed_domains = ["repositorio.ufpa.br"]
    start_urls = ["https://repositorio.ufpa.br/jspui/htmlmap"]

    def parse(self, response):
        links_sitemap = response.css("li a::attr(href)").extract()

        for i in range(10):
            yield scrapy.Request(url=links_sitemap[i], callback=self.get_page_links)

    def get_page_links(self, response):
        links_page = response.css("li a::attr(href)").extract()

        for i in range(len(links_page)):
            yield scrapy.Request(url=links_page[i], callback=self.open_link)

    def open_link(self, response):
        yield scrapy.Request(url=str(response), callback=self.get_details)

    def get_details(self, response):
        try:
            url = response.css("div.well code::text").get()
            tipo = response.css("td.dc_type a::text").get()
            data = response.css("td:nth-child(2).dc_date_issued::text").get()
            autores = response.css("td.dc_creator a::text").getall()
            titulo = response.css("td:nth-child(2).dc_title::text").get()
            resumo = response.css("td:nth-child(2).dc_description_resumo::text").get()
            palavras_chave = response.css("td:nth-child(2).dc_subject a::text").getall()
            repositorio = "UFPA"

            if consulta_de_palavra_em_texto(titulo, resumo, titulo, palavras_chave):
                documento = RepositoriosItem()
                documento["url"] = url
                documento["tipo"] = tipo
                documento["data"] = data
                documento["autores"] = autores
                documento["titulo"] = titulo
                documento["resumo"] = resumo
                documento["palavras_chave"] = palavras_chave
                documento["repositorio"] = repositorio
                yield documento
        except Exception as e:
            self.log(e)
