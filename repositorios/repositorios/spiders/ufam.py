import scrapy


class UfamSpider(scrapy.Spider):
    name = "ufam"
    allowed_domains = ["riu.ufam.edu.br"]
    start_urls = ["https://riu.ufam.edu.br/htmlmap"]

    def parse(self, response):
        links = response.css("li a::attr(href)").extract()

        for link in links[:4]:
            yield response.follow(link, callback=self.get_links)

    def get_links(self, response):
        links = response.css("li a::attr(href)").extract()

        for link in links:
            yield response.follow(link, callback=self.get_page)

    def get_page(self, response):
        table = response.xpath('//table[contains(@class, "table")]')

        titulo = table.xpath('//tr[2]/td[2]/text()').get()
        autores = list(set(table.xpath("//tr[3]/td[2]/a[@class='author']/text()").getall()))
        resumo = table.xpath("//tr[5]/td[2]/text()").get()
        palavras_chave = response.xpath("//tr[6]/td[2]/text()").extract()
        url = response.xpath("//div[2]/div[1]/code/text()").get()
        tipo = response.xpath("//tr[1]/td[2]/a/text()").get()
        data = response.xpath("//tr[16]/td[2]/text()").get()
        repositorio = "UFAM"

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
