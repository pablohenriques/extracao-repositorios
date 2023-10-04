import scrapy


class UfmtSpider(scrapy.Spider):
    name = "ufmt"
    allowed_domains = ["ri.ufmt.br"]
    start_urls = ["https://ri.ufmt.br/htmlmap"]

    def parse(self, response):
        links = response.xpath("/html/body/ul/li/a/@href").extract()
        for item in links:
            yield scrapy.Request(url=item, callback=self.get_links)
    
    def get_links(self, response):
        links = response.xpath("/html/body/ul/li/a/@href").extract()
        for item in links:
            yield scrapy.Request(url=item, callback=self.get_details)
    
    def get_details(self, response):
        try:
            body = response.xpath("/html/body")
            table = body.xpath("//main/div/table")

            tipo = table.xpath("//tr/td[contains(@class, 'dc_type')]//following-sibling::td[contains(@class, 'dc_type')]/a/text()").extract_first()
            titulo = table.xpath("//tr/td[contains(@class, 'dc_title')]//following-sibling::td[contains(@class, 'dc_title')]/text()").extract_first()
            autores = table.xpath("//tr/td[contains(@class, 'dc_contributor_author')]//following-sibling::td[contains(@class, 'dc_contributor_author')]/a/text()").getall()
            resumo = table.xpath("//tr/td[contains(@class, 'dc_description_abstract')]//following-sibling::td[contains(@class, 'dc_description_abstract')]/text()").extract_first()
            palavras_chave = table.xpath("//tr/td[contains(@class, 'dc_subject') and not(contains(@class, 'dc_subject_cnpq'))]//following-sibling::td[contains(@class, 'dc_subject')]/text()").getall()
            repositorio = "UFV"
            url = table.xpath("//tr/td[contains(@class, 'dc_identifier_uri')]//following-sibling::td[contains(@class, 'dc_identifier_uri')]/a/text()").extract_first()
            data = table.xpath("//tr/td[contains(@class, 'dc_date_issued')]//following-sibling::td[contains(@class, 'dc_date_issued')]/text()").extract_first()

            yield {
                'autores': autores,
                'data': data,
                'palavras_chave': palavras_chave,
                'repositorio': repositorio,
                'resumo': resumo,
                'titulo': titulo,
                'tipo': tipo,
                'url': url
            }

        except Exception as e:
            self.log(e)

