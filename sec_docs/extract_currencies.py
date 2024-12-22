
import os
import json

#files = os.listdir('/home/diego/projects/sec_docs/companyfacts/')
files = os.listdir('./companyfacts/')

for element in files:
    f = open('./companyfacts/'+element)
    data = json.load(f)
#    print(data.keys())
    currency = list(data.get('facts',{}).get('us-gaap',{}).get('Revenues',{}).get('units',{}).keys())
    if len(currency) > 0:
        if currency[0] != 'USD':
            print(data['cik'])
            print(data['entityName'])
            print(currency)
    f.close()


