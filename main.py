from bs4 import BeautifulSoup
from googlesearch import search
import requests
import re


with open('proxy.txt', 'w') as f:
    for sites in search("free proxy server", tld="co.in", num=1000, stop=1000, pause=2): #pesquisa por"freeproxyserver" no google
        data = requests.get('{url}'.format(url=sites))
        proxys = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)', data.text)
        for proxy in proxys: 
            f.write(str(proxy)) #guarda no file "proxy.txt"
