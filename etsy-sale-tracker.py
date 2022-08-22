import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime  


def salechecker():
  URL = 'https://www.etsy.com/shop/PearlPrestigePlanner'
  header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
  sayfa = requests.get(URL, headers = header)
  contentparser = BeautifulSoup(sayfa.content,'html.parser')
 
#we are going to find store name with the code below
  dukkanadi = contentparser.find("h1", {"class":"wt-text-heading-01 wt-text-truncate"}).text

#we are going to find sale numbers with the code below
  satisadet = contentparser.find("span", {"class":"wt-text-caption wt-no-wrap"}).text.split()

  satisstr = satisadet[0].replace(',','')
  
#finding the date
  tarih = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
  print(f"{dukkanadi} Etsy dükkanı \n{tarih} tarihinde yapılan kontrolde {satisstr} adet satış yapmıştır.")


  

while(True):
  salechecker()
  time.sleep(60*60*24)





