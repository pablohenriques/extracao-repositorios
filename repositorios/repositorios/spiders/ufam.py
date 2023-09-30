import scrapy


class UfamSpider(scrapy.Spider):
    name = "ufam"
    allowed_domains = ["riu.ufam.edu.br"]
    start_urls = ["https://riu.ufam.edu.br/htmlmap"]

    def parse(self, response):
        links_sitemap = response.css("li a::attr(href)").extract()

        for i in range(1):
            yield scrapy.Request(url=links_sitemap[i], callback=self.get_page_links)

    def get_page_links(self, response):
        links_page = response.css("li a::attr(href)").extract()

        for i in range(1):
            yield scrapy.Request(url=links_page[i], callback=self.open_link)

    def open_link(self, response):
        yield scrapy.Request(url=response, callback=self.get_details)

    def get_details(self, response):
        self.log(response)