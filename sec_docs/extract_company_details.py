import os
import json
import pandas as pd


dir = './companies'
files = os.listdir(dir)


dict_data = {'cik':list(),
        'entityType':list(),
        'sic':list(),
        'sicDescription':list(),
        'name':list(),
        'tickers':list(),
        'exchanges':list(),
        'ein':list(),
        'description':list(),
        'category':list(),
        'fiscalYearEnd':list()}

for elem in files:
    if elem[-4:] == 'json':
        print(elem)
        f = open(dir+'/'+elem)
        data = json.load(f)
        
        dict_data['cik'].append(data.get('cik',''))
        dict_data['entityType'].append(data.get('entityType',''))
        dict_data['sic'].append(data.get('sic',''))
        dict_data['sicDescription'].append(data.get('sicDescription',''))
        dict_data['name'].append(data.get('name',''))
        dict_data['tickers'].append(data.get('tickers',''))
        dict_data['exchanges'].append(data.get('exchanges',''))
        dict_data['ein'].append(data.get('ein',''))
        dict_data['description'].append(data.get('description',''))
        dict_data['category'].append(data.get('category',''))
        dict_data['fiscalYearEnd'].append(data.get('fiscalYearEnd',''))

        f.close()

df = pd.DataFrame(dict_data)
df.to_csv('aggreg_data.csv')



