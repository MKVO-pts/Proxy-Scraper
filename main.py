from bs4 import BeautifulSoup
from googlesearch import search
import requests
import re
import subprocess

#Remove os seguintes caracteres: ()',
def cleanProxy(proxy):
    proxy = str( re.sub('[()\' ]','',str(proxy)) )
    proxy = str( re.sub(',',':',str(proxy)) )
    return proxy



with open('proxy.txt', 'w') as f:
    for website in search("free proxy server", tld="co.in", num=1000, stop=1000, pause=2): #pesquisa por"freeproxyserver" no google
        print("Searching in: "+website)
        data = requests.get('{url}'.format(url=website))
        proxys = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)', data.text)
        for proxy in proxys: 
            f.write(cleanProxy(proxy)+"\n") #guarda no file "proxy.txt"
            print("Proxy Found: "+cleanProxy(proxy))
            print("Ping to: "+cleanProxy(proxy)+" whit status: "+str( subprocess.call('ping '+cleanProxy(proxy)) ))
    

