import json
import requests
import time


hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

data_elements = ['Revenues']

for elm in data_elements:
    print("Sleep 10 seconds.")
    time.sleep(10)
    r = requests.request(method='get',
            url='https://data.sec.gov/api/xbrl/frames/us-gaap/'+elm+'/USD/CY2022.json',
            headers=hdr)
    print(r)
    if r.ok:
        print("ok")
        data = r.json()

        print(data.keys())
        print("data")
        print(data['data'].keys())
"""
    with open('sec_data/'+elm+'.csv','wb') as f:
        f.write()
"""


