# Proxy-Scraper

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Python Libraries](#pytho-libraries)

## General info
This file will look for sites whit proxys using Google and then it will store them in a file``proxys.txt``.
There is no need to configure anything. It work whit Linux and Termux.

## Setup
first use git clone to download the project, then run the install.sh
```
$ git clone https://github.com/MKVO-pts/Proxy-Scraper.git
$ cd Proxy-scraper
$ bash install.sh
```
## Features
This project do:
* Scrape sites from the internet
* Scrape the proxies automatically
* Remove the repeated proxies 
* Grab info about them (ping,country,city...)

## Python libraries
This project use the following modules:
* google (googlesearch)
* bs4 (BeautifulSoup)
* ipwhois
* random
* requestes
* re
* subprocess
* time
* pysimplegui

## Required programs
This project use the following programs:
* nmap
* proxychains (optional)
