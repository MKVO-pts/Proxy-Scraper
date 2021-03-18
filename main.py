from bs4 import BeautifulSoup
from googlesearch import search
from ipwhois import IPWhois
import requests
import subprocess
import random
import json
import time
import re

#classe para tirar info das proxys
#a que stou a usar atualmente pode n ser a melhor, mas ao menos n temos de a criar ficheiros para cache
class InfoGraver:                              #classe para tirar info
	def __init__(self, ip):
		self.proxy = proxy
		self.info = IPWhois(f'{ip}')
		self.geral = self.info.lookup_whois()
	def infos(self):

		pais = self.geral['nets'][0]['country']
		cidade = self.geral['nets'][0]['city']
		ip_f = self.geral['query']
		velocidade = "10 ms" #ainda n fiz 

		data = {  #tipo de data no final
			'proxy':f'{ip_f}',
			'pais':f'{pais}',
			'cidade':f'{cidade}',
			'velocidade':f'{velocidade}'
		}
		return data

    
    
quantSearchs = int( input("Number of Sites to search: ") )      
FakeWebsites = [i.strip().split() for i in open("FakeWebsites.txt").readlines()]
    
for website in search("free proxy server", tld="co.in", num=quantSearchs, stop=quantSearchs, pause=3): #pesquisa por"freeproxyserver" no google
    if any(website in s for s in FakeWebsites):
        continue
    print("Searching in: "+website)
    data = requests.get('{url}'.format(url=website))                                                   #tira a info do site
    scraped = re.findall(r'((?:\d{1,3}\.){3}\d{1,3}[:]\d+)', data.text)                                #filtra as proxys do site
    proxys = list(dict.fromkeys(scraped))                                                              #remove as proxys repetidas     
    
    if(proxys): #se existirem proxys no site
        for proxy in proxys:  #loop para cada proxy no site
            
            #nmap -p , nas proxys
            ip, port = proxy.split(":")
            status = str(subprocess.check_output(["nmap", "-p", f"{port}", f"{ip}"]))
            
            #filtra apenas as que estao vivas
            if "Host is up " in status:                     #verifica se a frase aparece quando usamos o comando do nmap
	            print(f'{proxy} is Alive')
                
                #saca info das proxys que estao "Alive"
                print(InfoGraver(ip).infos())
                
                
                #guarda as proxys
                with open('proxy.txt', 'a') as f: 
                    f.write(proxy+"\n")                                 #guarda no file "proxy.txt"
            
            elif "Note: Host seems down." in status:
	            print(f'{proxy} is Dead')

            else:    #se nao estiver dead ou alive
            	print('Erro desconhecido')
 
            
    else:
        with open('FakeWebsites.txt', 'a') as f_2:
            f_2.write(website + "\n")                                #adiciona os sites sem proxys ao ficheiro de text
    
    #timeout para evitar passar o limit de requests
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
