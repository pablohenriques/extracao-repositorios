import scrapy


class UfpaSpider(scrapy.Spider):
    name = "ufpa"
    allowed_domains = ["repositorio.ufpa.br"]
    start_urls = ["https://repositorio.ufpa.br/jspui/htmlmap"]

    def parse(self, response):
        links_sitemap = response.css("li a::attr(href)").extract()

        for link in links_sitemap:
            yield scrapy.follow(link, callback=self.get_page_links)

    def get_page_links(self, response):
        links_page = response.css("li a::attr(href)").extract()

        for link in links_page:
            yield scrapy.follow(link, callback=self.get_details)

    def get_details(self, response):
        url = response.css("div.well code::text").get()
        tipo = response.css("td.dc_type a::text").get()
        data = response.css("td:nth-child(2).dc_date_issued::text").get()
        autores = response.css("td.dc_creator a::text").getall()
        titulo = response.css("td:nth-child(2).dc_title::text").get()
        resumo = response.css("td:nth-child(2).dc_description_resumo::text").get()
        palavras_chave = response.css("td:nth-child(2).dc_subject a::text").getall()
        repositorio = "UFPA"


