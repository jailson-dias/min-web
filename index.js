import express from 'express';
import bodyParser from 'body-parser';
import http from 'http';
import { NaturalLanguageUnderstandingV1 } from 'watson-developer-cloud';

let app = express();

app.set('port', process.env.PORT || 3000);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const naturalLanguageUnderstanding = new NaturalLanguageUnderstandingV1({
  version: '2018-11-06',
  iam_apikey: 'nWIUdYcZDqxWnqhz3ACTynS5zsZqdI9MlOcS4WexgyCl',
  url: 'https://gateway.watsonplatform.net/natural-language-understanding/api'
});

app.post('/analyze', (req, res) => {
  const urls = req.body

  const parameters = {
    'url': 'https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-cirurgia-bariatrica/',
    'features': {
      'entities': {
          'model': '9c4ed27b-d7cb-4d64-b73f-80eaab7b939d'
      }
    }
  };

  naturalLanguageUnderstanding.analyze(parameters, (error, response) => {
    if (!error) {
      res.status(200).json(response);
    } else {
      console.log(error);
      res.status(500).json({ message: 'internal server error' });
    }
  })
});

const port = app.get('port');
http.createServer(app).listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});

var urls = [
  ['https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-diabetes/', 'diabetes'],
  ['https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-obesidade/', 'obesidade'],
  ['https://www.endocrino.org.br/10-coisas-que-voce-precisa-saber-sobre-hipertensao/', 'hipertensao'],
  ['https://www.tuasaude.com/diabetes-tipo-2/', 'diabetes'],
  ['https://www.tuasaude.com/o-que-comer-na-diabetes/', 'alimentacao'],
  ['http://prevencao.cardiol.br/fatores-de-risco/hipertensao.asp', 'hipertensao'] 
]
