from bs4 import BeautifulSoup
from googlesearch import search
import requests
import re
import subprocess
import time
import random

quantSearchs = int( input("Number of Sites to search ") )
#Remove os seguintes caracteres: ()',
def cleanProxy(proxy):
    proxy = str( re.sub('[()\' ]','',str(proxy)) )
    proxy = str( re.sub(',',':',str(proxy)) )
    return proxy


FakeWebsites = [i.strip().split() for i in open("FakeWebsites.txt").readlines()]


for website in search("free proxy server", tld="co.in", num=quantSearchs, stop=quantSearchs, pause=2): #pesquisa por"freeproxyserver" no google
    if any(website in s for s in FakeWebsites):
        continue
    print("Searching in: "+website)
    data = requests.get('{url}'.format(url=website))
    proxys = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)', data.text)
    if(proxys):
        for proxy in proxys:
            with open('proxy.txt', 'a') as f: 
                f.write(cleanProxy(proxy)+"\n") #guarda no file "proxy.txt"
                print("Proxy Found: "+cleanProxy(proxy))
                print("Ping to: "+cleanProxy(proxy)+" whit status: "+str( subprocess.call('nmap -p {port} {ip} '.format(port=cleanProxy(proxy).split(':')[1], ip=cleanProxy(proxy).split(':')[0])) ))
    else:
        with open('FakeWebsites.txt', 'a') as f_2:
            f_2.write(cleanProxy(website)+"\n")

    timewait = random.randint(30,60)
    print("Waiting"+str(timewait)+" seconds")
    time.sleep(timewait)
    

