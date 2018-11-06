const fs = require('fs');
const NaturalLanguageUnderstandingV1 = require('watson-developer-cloud/natural-language-understanding/v1.js');

var naturalLanguageUnderstanding = new NaturalLanguageUnderstandingV1({
  version: '2018-11-06',
  iam_apikey: 'nWIUdYcZDqxWnqhz3ACTynS5zsZqdI9MlOcS4WexgyCl',
  url: 'https://gateway.watsonplatform.net/natural-language-understanding/api'
});

var parameters = {
  'url': 'https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-cirurgia-bariatrica/',
  'features': {
    'entities': {
        'model': '9c4ed27b-d7cb-4d64-b73f-80eaab7b939d'
    }
  }
};

naturalLanguageUnderstanding.analyze(parameters, function(err, response) {
  if (err) {
    console.log('erro requisitando a api do watson:', err);
  } else {
    fs.writeFile("./output.json", JSON.stringify(response, null, 4), function(err) {
        if(err) {
            return console.log("erro salvando o arquivo", err);
        }
        console.log("Documento avaliado com sucesso!!");
    }); 
  }

});
