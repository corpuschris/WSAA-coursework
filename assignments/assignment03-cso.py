import requests

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'
response = requests.get(url)

with open('cso.json', 'w') as file:
    file.write(response.text)

print("Dataset saved as cso.json")