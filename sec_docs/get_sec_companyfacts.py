import requests 

hdr = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

r = requests.request(method='get',url='http://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip',headers=hdr)

with open('company_facts.zip', 'wb') as f:
    f.write(r.content)


