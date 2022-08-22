import requests
from bs4 import BeautifulSoup
import time


URL = 'https://www.etsy.com/shop/PearlPrestigePlanner'
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
sayfa = requests.get(URL, headers = header)
icerik = BeautifulSoup(sayfa.content,'html.parser')
    #print(icerik)
    #productTitle

dukkanadi = icerik.find("h1", {"class":"wt-text-heading-01 wt-text-truncate"}).text
#print(dukkanadi)

    #priceblock_ourprice

satisadet = icerik.find("span", {"class":"wt-text-caption wt-no-wrap"}).text.split()

satisstr = satisadet[0].replace(',','')
    #ucretDonusturen = int(ucreti[1:6].replace('.',''))
#print(satisstr)

print(f"{dukkanadi} Etsy dükkanı {satisstr} adet satış yapmıştır.")

   # if(ucretDonusturen < 8000):
      #  print(f"{ucretDonusturen} TL {urunAdi} fiyatı düştü acele et!!!")
    #else:
     #   print(f"{ucretDonusturen} TL {urunAdi} henüz düşmedi")

#while(True):
 #   urunKontrolEt()
  #  time.sleep(3)





