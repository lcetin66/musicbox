import sqlite3

import time



class Sarki():

    def __init__(self, isim, sanatci, album, yapim, sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.yapim = yapim
        self.sure = sure

    def __str__(self):
        return "Sarki ismi\t: {}\nSanatci\t\t: {}\nAlbum\t\t: {}\nYapim Sirketi\t: {}\nSarki suresi\t: {}\n".format(self.isim, self.sanatci, self.album, self.yapim, self.sure)


class Parcalar():

    def __init__(self):
        self.baglanti_kur()

    def baglanti_kur(self):

        self.con = sqlite3.connect("parcalar.db")
        self.cursor = self.con.cursor()
        soru = "CREATE TABLE IF NOT EXISTS sarkilar (isim TEXT,sanatci TEXT,album TEXT,yapim TEXT,sure NUMERIC)"
        self.cursor.execute(soru)
        self.con.commit()

    def baglantiyi_kes(self):

        self.con.close()

    def sarkilari_goster(self):
        soru = "SELECT * FROM sarkilar"
        self.cursor.execute(soru)
        parcalar = self.cursor.fetchall()

        if (len(parcalar) == 0):
            print("Kütüphanede parca bulunmuyor...\n")

        else:
            for i in parcalar:
                sarki = Sarki(i[0], i[1], i[2], i[3], i[4])
                print(sarki)

    
    def sarki_ekle(self, sarki):
        soru = "INSERT INTO sarkilar VALUES (?,?,?,?,?)"
        self.cursor.execute(soru, (sarki.isim,sarki.sanatci,sarki.album,sarki.yapim,sarki.sure))
        self.con.commit()
        
    
    def sarki_sil(self, isim):
        soru="SELECT * FROM sarkilar WHERE isim = ?"
        self.cursor.execute(soru,(isim,))
        parcalar = self.cursor.fetchall()
        
        if (len(parcalar)==0):
            print("Böyle bir sarki bulunmuyor\n")
            
        else:
            cevap = input("Emin misiniz? (E/H)")

            if (cevap == "E" or cevap == "e"):
                print("Sarki siliniyor...")
                time.sleep(2)
                
                sorgu2 = "DELETE FROM sarkilar WHERE isim = ?"
                self.cursor.execute(sorgu2, (isim,))
                self.con.commit()
                print("Sarki silindi...\n")
                self.sarkilari_goster()

    
    def sarkilarin_suresi(self):
        soru = "SELECT * FROM sarkilar"
        self.cursor.execute(soru)
        parcalar = self.cursor.fetchall()

        if (len(parcalar) == 0):
            print("Kütüphanede parca bulunmuyor...")
        
        else:
            toplam=0
            for i in parcalar:
                print(i[0]," :", i[4])
                sure=sum(int(x) * 60**index for index,
                         x in enumerate(i[4].split(":")[::-1]))
                toplam+=sure
            
            dk, sn = divmod(toplam, 60)
            # sa, dk = divmod(dk, 60)
            # print ("Toplam: %d:%02d:%02d" % (sa, dk, sn))
            print("Toplam\t: %02d:%02d\n" % (dk, sn))