from bs4 import BeautifulSoup
from googlesearch import search
import requests
import subprocess
import time
import random
import re

quantSearchs = int( input("Number of Sites to search: ") )      
FakeWebsites = [i.strip().split() for i in open("FakeWebsites.txt").readlines()]


for website in search("free proxy server", tld="co.in", num=quantSearchs, stop=quantSearchs, pause=2): #pesquisa por"freeproxyserver" no google
    if any(website in s for s in FakeWebsites):
        continue
    print("Searching in: "+website)
    data = requests.get('{url}'.format(url=website))                                                   #tira a info do site
    scraped = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}[:]\d+)', data.text)                                #filtra as proxys do site
    proxys = list(dict.fromkeys(scraped))                                                              #remove as proxys repetidas     
    if(proxys):
        for proxy in proxys:
            with open('proxy.txt', 'a') as f: 
                f.write(proxy+"\n")                                 #guarda no file "proxy.txt"
                print("Proxy Found: ",proxy)
    else:
        with open('FakeWebsites.txt', 'a') as f_2:
            f_2.write(website + "\n")                                #adiciona os sites sem proxys ao ficheiro de text

    timewait = random.randint(30,60)
    print("Waiting "+str(timewait)+" seconds")
    time.sleep(timewait)


#with open('proxy.txt', 'w') as f:
    
    #for website in search("free proxy server", tld="co.in", num=1000, stop=1000, pause=2): #pesquisa por"freeproxyserver" no google
        #print("Searching in: "+website) 
        #data = requests.get('{url}'.format(url=website))                     
        #proxys = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}[:]\d+)', data.text)      #procura por proxies no site
        #for proxy in proxys: 
            

            #f.write(proxy+"\n")                             #guarda no file "proxy.txt"
            #print("Proxy Found: "+proxy)
  
            #clean = proxy.split(':')[0]                      #ip sem a porta
            #print("Ping to: "+proxy+" whit status: " + str( subprocess.call('ping '+ proxy )))

    


            #f.write(proxy+"\n")                           #guarda no file "proxy.txt"
            #print("Proxy Found: "+proxy)
            
            #print("Ping to: "+proxy+" whit status: " + str( subprocess.call('nmap -p {port} {ip}'.format(porta=proxy.split(':')[1], ip=proxy.split(':')[0])))
