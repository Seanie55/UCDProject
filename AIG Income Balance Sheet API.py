import requests

request = requests.get('https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=AIG&apikey=G9XKT7Z448L4T6EY')

data = request.json()

for p in data['annualReports']:
    print("Year:  ", p['fiscalDateEnding'])
    print("Total Assets: ", p['totalAssets'])
    print("Total Liabilities: ", p['totalLiabilities'])


