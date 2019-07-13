import json
from urllib.request import urlopen

# Using the WorldTrading Data API 
#with urlopen("https://api.worldtradingdata.com/api/v1/history?symbol=MSFT&api_token=EI7djkhnw9BIIJ9E1ionc8PFVWpjcWRUIvI1EMZYgn7QDA898Y7jC9YD8yhd") as response:
#    source = response.read()
with open('microsoft_history.json')as f:
    data = json.load(f)
#data = json.load(source)
print(data['history'])
print(len(data['history']))
print(type(data))
f#or item in data['history']:
#    print(item)
#    for value in item:
#        print(value)
#    date = data['history']
#    volume = item[4]
#    print(date,volume)

#print(json.dumps(data,indent = 2))
#with open('microsoft_history.json','w') as f:
#    json.dump(data,f, indent=2)