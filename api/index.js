import express from 'express';
import bodyParser from 'body-parser';
import http from 'http';
import { NaturalLanguageUnderstandingV1,
         NaturalLanguageClassifierV1,
         DiscoveryV1 } from 'watson-developer-cloud';
         
let app = express();

app.set('port', process.env.PORT || 3000);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const naturalLanguageUnderstanding = new NaturalLanguageUnderstandingV1({
  version: '2018-11-06',
  iam_apikey: '',
  url: ''
});

const naturalLanguageClassifier = new NaturalLanguageClassifierV1({
  iam_apikey: '',
  url: ''
});

const discovery = new DiscoveryV1({
  version: '2018-12-03',
  iam_apikey: '',
  url: ''
});

app.post('/analyze', (req, res) => {
  const urls = req.body

  const parameters = {
    'url': '',
    'features': {
      'entities': {
          'model': ''
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

app.post('/classify', (req, res) => {
  const text = req.body.text;

  naturalLanguageClassifier.classify({
    text,
    classifier_id: '' },
    function(err, response) {
      if (err) {
        console.log('error:', err);
        res.status(500).json({message: 'internal server error'})
      } else {
        res.status(200).json(response);
      }
  });
});

app.post('/sumarize', (req, res) => {
  discovery.query({
    environment_id: '',
    collection_id: '',
    natural_language_query: 'qual a parte mais relevante do texto?',
  }, (err, response) => {
    if (err) {
      console.log('error: ', err);
      res.status(500).json({ message: 'internal server error' });
    } else {
      res.status(200).json(response);
    }
  });
});

const port = app.get('port');
http.createServer(app).listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});

