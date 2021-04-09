from _Muzik import *

print("""
*********************************

Muzikbox'a Hosgeldiniz.

Islemler;
1. Sarkilari Göster
2. Sarki ekle
3. Sarki Sil
4. Parca Süreleri

Cikmak icin 'q' basin

********************************
""")
parcalar = Parcalar()

while True:

    islem = input("Yapacaginiz islemi secin: ")

    if (islem == "q" or islem == "Q"):
        print("Islem Solandiriliyor....")
        print("Yine Bekleriz...")
        break
    elif (islem == "1"):
        parcalar.sarkilari_goster()
    elif (islem == "2"):
        isim = input("Isim: ")
        sanatci = input("Sanatci: ")
        album = input("Albüm: ")
        yapim = input("Yapim Sirketi: ")
        sure = input("Süre: ")

        sarki = Sarki(isim, sanatci, album, yapim, sure)

        print("Sarki ekleniyor...")
        time.sleep(2)

        parcalar.sarki_ekle(sarki)
        print("Yeni sarki eklendi...")

    elif (islem == "3"):
        isim = input("Hangi sarkiyi silmek istiyorsunuz? ")
        parcalar.sarki_sil(isim)
    elif (islem == "4"):
        parcalar.sarkilarin_suresi()
