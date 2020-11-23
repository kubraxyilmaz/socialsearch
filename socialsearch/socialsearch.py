import random
import webbrowser
import requests
from bs4 import BeautifulSoup

baseUrl = "https://facebook.com/"
#eğer instagram üzerinden tarama yapılacaksa https://instagram.com/
karakterListesi = "0123456789abcdefghijklmnopqrstuvwxyz._"

kullaniciAdi=input("Lütfen kullanıcı adını giriniz: ")
eklenenKarakter = input("Lütfen kullanıcı adı sonuna eklenecek maksimum karakter sayısını giriniz: ")
donguSayisi = input("Lütfen kaç deneme yapılacağını giriniz: ")
eklenenKarakter=int(eklenenKarakter)
yedekUzanti=""
for a in range(1,int(eklenenKarakter+1)):
    for x in range(int(donguSayisi)):
        uzanti = ""
        uzanti=random.sample(karakterListesi,a)
        uzantiFull=''.join(uzanti)
        if(uzantiFull != yedekUzanti):
            yedekUzanti=''.join(uzanti)
            url=baseUrl+kullaniciAdi+uzantiFull
            print("Denenen url: ",url)

            r = requests.get(url)

            if r.status_code==200:
                print("Hesap bulundu ve başarı ile txt'ye yazıldı.")
                dosya1 = open("Hesaplar.txt", "a")
                dosya1.write(url+"\n")
                dosya1.close()
    
            else:
                print("Hesap bulunamadı.")
                print("Hata Kodu: ",r.status_code)
        

    
