import json

with open('labelsjson2.json') as f:
    data = json.load(f)

hits = 0
for i in data:
    if i['label'] == i['watsonLabel']:
        hits += 1

print(hits/len(data))
