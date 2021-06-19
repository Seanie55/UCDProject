import requests

request = requests.get('http://api.open-notify.org/astros.json')

data = request.json()

print("Total Amount of People currently in Space = ", data['number'])
for p in data['people']:
    print("NAME:  ", p['name'])
    print("CRAFT: ", p['craft'])





