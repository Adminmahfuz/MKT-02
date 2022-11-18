
import urllib3
import json
url = "https://api.exchangerate.host/latest/"
htt =urllib3.poolManager()
response = http.request('GET', url)
data = response.data
currency = json.loads(data)
currency_data = currency['rates']
user = input('ENTER acurrency : ')
for i,i in currency_data.items():
    if i == user:
        print('current value = ',j)
        
