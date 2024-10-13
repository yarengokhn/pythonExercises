 
# print("mesaj: ")
# mesaj = input()
# print("merhaba BTK akademi "+mesaj)
urunAFiyat = 2000
print(urunAFiyat + ( urunAFiyat * 0.18))
_sayi1 = 20
# camelcase ,case sensitive
x,y,z = 10,20,30

"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Sadık Turan
05321234567
info@sadikturan.com
Kocaeli

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 550 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""

musteriIsim ="Sadık"
musteriSoyisim = "Turan"
musteriTel = "05321234567"
musteriEmail = "info@sadikturan.com"
musteriAdres = "Kocaeli"

urunAdi1, urunAdi2, urunAdi3= "Kablosuz Mouse","Kablosuz Klavye","Dizüstü Bilgisayar"

urun1Fiyat,urun2Fiyat,urun3Fiyat = 550,650,55000


toplamOdenenUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat

print("Toplam ödenen miktar: " + str(toplamOdenenUcret))

print("Toplam kdv oranı :"+ str(toplamOdenenUcret * 0.18))


"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""

yariCap =float(input("Yarıçap :"))

pi = 3.14

alan = pi * (yariCap ** 2)

cevre = 2*pi*yariCap

print("Alan: " + str(alan))
print("Çevre : " + str(cevre))

message =float(input("km : "))

mil = float(message/1.609344)

mil =round(mil,2)

print("MİL :"+ str(mil))

