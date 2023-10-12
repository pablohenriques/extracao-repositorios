import scrapy


class UftSpider(scrapy.Spider):
    name = "uft"
    allowed_domains = ["repositorio.uft.edu.br"]
    start_urls = ["https://repositorio.uft.edu.br/htmlmap"]

    def parse(self, response):
        links = response.css("li a::attr(href)").extract()

        for link in links[0]:
            yield response.follow(link, callback=self.get_links)

    def get_links(self, response):
        links = response.css("li a::attr(href)").extract()

        for link in links:
            yield response.follow(link, callback=self.get_links)

    def get_page(self, response):
        titulo = response.css("td:nth-child(2).dc_title::text").get()
        resumo = response.css("td:nth-child(2).dc_description_resumo::text").get()
        palavras_chave = response.css("td:nth-child(2).dc_subject a::text").getall()
        url = response.css("div.well code::text").get()
        tipo = response.css("td.metadataFieldValue a::text").get()
        data = response.css("td:nth-child(2).dc_date_issued::text").get()
        autores = response.css("td:nth-child(2).dc_contributor_author::text").getall()
        repositorio = "UFT"

        yield {
            "titulo": titulo,
            "resumo": resumo,
            "palavras_chave": palavras_chave,
            "url": url,
            "tipo": tipo,
            "data": data,
            "autores": autores,
            "repositorio": repositorio
        }
