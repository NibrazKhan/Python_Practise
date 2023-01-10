import json
from urllib.request import urlopen

with urlopen("https://open.er-api.com/v6/latest/USD") as response:
    source = response.read()
# Parsing json object into python object
data = json.loads(source)
# Printing a json in a more readable formatted way
print(json.dumps(data, indent=2))
# for currency_type in data['rates']:
#     print("Rate of "+currency_type+" is "+ str(data['rates'][currency_type]),end='\n')
# Another way of doing the same thing:
# for currency_type,value in data['rates'].items():
#     print("Rate of " + currency_type + " is " + str(value), end='\n')
# rates=data['rates']
# def currency_conversion(USD,currency_type):
#     converted_currency=USD*rates[currency_type]
#     print("Converted currency:",converted_currency)
#
# currency_conversion(100,"BDT")