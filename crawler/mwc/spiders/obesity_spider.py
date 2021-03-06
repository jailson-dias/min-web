#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy, json, re

terms = [
'glicose',
'pressao-aeterial',
'hipertensão',
'acucar',
'gordura',
'peso',
'Obesidade',
'cirurgia-bariatrica',
'coração',
'pancreas',
'estomago',
'colesterol',
'gastrite',
'doenca-cardio-vascular',
'cardiaco',
'morbidade',
'morbido',
'Gordo',
'triglicerídeo',
'fígado',
'alcoolismo',
'insulina',
'Imc',
'comida',
'alimentacao-saudavel',
'frutas',
'hdl',
'ldl',
'bariátrica',
'estomago',
'apneia',
'Peso',
'Strogonoff',
'Lasanha',
'Macarronada',
'Fruta',
'sobrepeso',
'Aveia',
'Fibras', 
'Cereais', 
'Verdura', 
'Proteína',
'Carboidrato',
'Dieta',
'Hérnia',
'Laparoscopia',
'dor-nas-juntas',
'Infarto',
'coronaria',
'gastrico',
'Gastro',
'Nutricionista', 
'Cardiologista',
'Granola',
'Manga', 
'Cha-verde',
'Emagrece',
'Chá preto',
'Chia',
'Lichia',
'Jamelão',
'Aveia',
'Glicosimetro',
'Esfigmomanometro',
'Artrose',
'Fertilidade',
'Sexo',
'Osteoporose',
'Entalamento',
'Entalar',
'Nausea',
'Vomito',
'Hemoglobina glicada',
'Hiperglicemia',
'Hipoglicemia',
'Pre-diabetico',
'Diabetico',
'Cigarro',
'Fumo',
'Tabagismo' 
]

class ObesitySpider(scrapy.Spider):
    name = 'obesity'
    allowed_domains = [
        'saudebemestar.com.pt', 
       'www.tuasaude.com', 
    ]
    start_urls = [
        'https://saudebemestar.com.pt/category/nutricao-e-exercicio/',
        'https://saudebemestar.com.pt/category/prevencao-e-vida-saudavel/',
        'https://www.tuasaude.com/diabetes-tipo-2/',
    ]

    def get_text(self, response):
        text = ''
        paragraphs = response.xpath("//p")
        for p in paragraphs:
            paragraph = p.xpath("text()").extract_first()
            if paragraph != None:
                text = text + paragraph + '\n'
        return text

    def save(self, response):
        file = open("/src/pages/list", 'a')
        file.write(response.url + '\n')
        file.close()
        domain = response.url.split('/')[2]
        file = open("/src/pages/jsons/" + response.url.replace('/', '_') + '.json', 'w')
        data = {"url": response.url, "text": self.get_text(response)}
        file.write(json.dumps(data))
        file.close()

    def is_article(self, response):
        if response.url.split('/')[2] in ['saudebemestar.com.pt', 'www.tuasaude.com', 'www.endocrino.org.br']:
            if response.url.count('/') == 4 and response.url.count('?') == 0:
                ret = 0
                words = re.sub("[^\w]", " ",  self.get_text(response)).split()
                for uword in words:
                    word = uword.lower()
                    if word in terms:
                        ret = ret + 1
                return ret >= 5
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
