import scrapy

class ObesitySpider(scrapy.Spider):
    name = 'obesity'
    allowed_domains = [
        'saudebemestar.com.pt', 
        'www.tuasaude.com', 
        'www.endocrino.org.br',
    ]
    start_urls = [
        'https://saudebemestar.com.pt/category/nutricao-e-exercicio/',
        'https://saudebemestar.com.pt/category/prevencao-e-vida-saudavel/',
        'https://www.tuasaude.com/diabetes-tipo-2/',
        'https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-hipertensao/',
    ]

    def save(self, response):
        file = open("/src/pages/list", 'a')
        file.write(response.url + '\n')
        file.close()

    def is_article(self, response):
        if response.url.split('/')[2] in ['saudebemestar.com.pt', 'www.tuasaude.com', 'www.endocrino.org.br']:
            if response.url.count('/') == 4 and response.url.count('?') == 0:
                return True
        return False

    def parse(self, response):
        print("URL", response.url)
        if self.is_article(response):
            self.save(response)
        a_selectors = response.xpath("//a")
        for selector in a_selectors:
            text = selector.xpath("text()").extract_first()
            link = selector.xpath("@href").extract_first()
            request = response.follow(link, callback=self.parse)
            yield request

