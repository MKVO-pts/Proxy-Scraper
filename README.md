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
$ bash install.sh (not done yet)
```
## Features
This project do:
* Send data about a member when requested(using discord bot commands)
* Track your war events (updated every 1min)
* Send a message when someone join/leave the clan ( MAX: 2 min delay)
* Create a amount of files whit info of every member who joined the cla (update every 3 min)

## Python libraries
This project use the following modules:
* google (googlesearch)
* bs4 (BeautifulSoup)
* requestes
* re
* subprocess
