import json
import requests

with open('./labelsjson.json')as f:
    data = json.load(f)

labels = []
for i in data:
    res = requests.api.post('http://localhost:3000/classify',json={'text': i['text']})
    res = res.json()
    confidence = res['classes'][0]['confidence']
    res = res['classes'][0]['class_name']
    i['watsonLabel'] = res
    i['watsonConfidence'] = confidence

with open('labelsjson2.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
