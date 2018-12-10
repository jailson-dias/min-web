import json
import csv
import os

def readJson(file):
    with open(file) as f:
        data = json.load(f)
        # print (data['url'] == 'https://ansjbfds.adsf.ds')
        # print (f.name)

        return [data['url'], data['text']]

def readCsv(file):
    with open(file) as f:
        data = csv.reader(f, delimiter=',')
        # for row in data:
        #     print (row)

        return list(data)

jsons = []
for fpath in os.listdir("./output/jsons_5words"):
    jsons.append(readJson("./output/jsons_5words/"+ fpath))
labels = readCsv('./output/list_5words')

base = []

for site in jsons:
    for label in labels:
        if (label[0] == site[0]):
            base.append({
                'url': site[0],
                'text': str(site[1].encode('utf-8').decode('utf-8')[:1024]),
                'label': label[1]
            })
            break

with open('./labelsjson.json', 'w') as f:
    json.dump(base, f, indent=4, ensure_ascii=False)

print (base)
