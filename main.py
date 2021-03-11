from bs4 import BeautifulSoup
from googlesearch import search
import requests
import subprocess
import numpy as np
import re




with open('proxy.txt', 'w') as f:
    
    for website in search("free proxy server", tld="co.in", num=1000, stop=1000, pause=2): #pesquisa por"freeproxyserver" no google
        print("Searching in: "+website) 
        data = requests.get('{url}'.format(url=website))                     
        proxys = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}[:]\d+)', data.text)      #procura por proxies no site
        for proxy in proxys: 
            
            f.write(proxy+"\n")                             #guarda no file "proxy.txt"
            print("Proxy Found: "+proxy)
  
            clean = proxy.split(':')[0]                      #ip sem a porta
            print("Ping to: "+proxy+" whit status: " + str( subprocess.call('ping '+ proxy )))
    

