#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy, json

terms = { 
    'diabetes': 'glicose',
    'hipertensao': 'pressao-aeterial',
    'hipertensao': 'hipertensão',
    'alimentacao': 'acucar',
    'alimentacao': 'gordura',
    'cirurgiaBariatrica': 'peso',
    'cirurgiaBariatrica': 'Obesidade',
    'cirurgiaBariatrica': 'cirurgia-bariatrica',
    'hipertensao': 'coração',
    'diabetes': 'pancreas',
    'cirurgiaBariatrica': 'estomago',
    'hipertensao': 'colesterol',
    'alimentacao': 'gastrite',
    'hipertensao': 'doenca-cardio-vascular',
    'hipertensao': 'cardiaco',
    'cirurgiaBariatrica': 'morbidade',
    'cirurgiaBariatrica': 'morbido',
    'cirurgiaBariatrica': 'Gordo',
    'alimentacao': 'triglicerídeo',
    'alimentacao': 'fígado',
    'cirurgiaBariatrica': 'alcoolismo',
    'diabetes': 'insulina',
    'cirurgiaBariatrica': 'Imc',
    'alimentacao': 'comida',
    'alimentacao': 'alimentacao-saudavel',
    'alimentacao': 'frutas',
    'alimentacao': 'hdl',
    'alimentacao': 'ldl',
    'cirurgiaBariatrica': 'bariátrica',
    'cirurgiaBariatrica': 'estomago',
    'cirurgiaBariatrica': 'apneia',
    'cirurgiaBariatrica': 'Peso',
    'alimentacao': 'Strogonoff',
    'alimentacao': 'Lasanha',
    'alimentacao': 'Macarronada',
    'alimentacao': 'Fruta',
    'cirurgiaBariatrica': 'sobrepeso',
    'alimentacao': 'Aveia',
    'alimentacao': 'Fibras', 
    'alimentacao': 'Cereais', 
    'alimentacao': 'Verdura', 
    'alimentacao': 'Proteína',
    'alimentacao': 'Carboidrato',
    'alimentacao': 'Dieta',
    'cirurgiaBariatrica': 'Hérnia',
    'cirurgiaBariatrica': 'Laparoscopia',
    'cirurgiaBariatrica': 'dor-nas-juntas',
    'hipertensao': 'Infarto',
    'hipertensao': 'coronaria',
    'cirurgiaBariatrica': 'gastrico',
    'cirurgiaBariatrica': 'Gastro',
    'alimentacao': 'Nutricionista', 
    'hipertensao': 'Cardiologista',
    'alimentacao': 'Granola',
    'alimentacao': 'Manga', 
    'alimentacao': 'Cha-verde',
    'alimentacao': 'Emagrece',
    'alimentacao': 'Chá preto',
    'alimentacao': 'Chia',
    'alimentacao': 'Lichia',
    'alimentacao': 'Jamelão',
    'alimentacao': 'Aveia',
    'diabetes':'Glicosimetro',
    'hipertensao': 'Esfigmomanometro',
    'cirurgiaBariatrica': 'Artrose',
    'cirurgiaBariatrica': 'Fertilidade',
    'cirurgiaBariatrica': 'Sexo',
    'cirurgiaBariatrica': 'Osteoporose',
    'cirurgiaBariatrica':'Entalamento',
    'cirurgiaBariatrica': 'Entalar',
    'cirurgiaBariatrica':'Nausea',
    'cirurgiaBariatrica': 'Vomito',
    'diabetes': 'Hemoglobina glicada',
    'diabetes': 'Hiperglicemia',
    'cirurgiaBariatrica': 'Hipoglicemia',
    'diabetes': 'Pre-diabetico',
    'diabetes': 'Diabetico',
    'cirurgiaBariatrica': 'Cigarro',
    'cirurgiaBariatrica': 'Fumo',
    'cirurgiaBariatrica':'Tabagismo' 
}

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

    def save(self, response):
        file = open("/src/pages/list", 'a')
        file.write(response.url + '\n')
        file.close()
        domain = response.url.split('/')[2]
        text = ''
        paragraphs = response.xpath("//p")
        for p in paragraphs:
            paragraph = p.xpath("text()").extract_first()
            if paragraph != None:
                text = text + paragraph + '\n'
        file = open("/src/pages/jsons/" + response.url.replace('/', '_') + '.json', 'w')
        data = {"url": response.url, "text": text}
        file.write(json.dumps(data))
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
