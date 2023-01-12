import sqlite3
import time

class Kitap():
    def __init__(self,kitapadi,yazar,yayinevi,tur,baski):
        self.kitapadi=kitapadi
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski

    def __str__(self):
        return " Kitap Adı : {} \n Yazarı : {}\n Yayın Evi : {}\n Türü : {}\n Baskısı : {}\n".format(self.kitapadi,self.yazar,self.yayinevi,self.tur,self.baski)

class Kutuphane():
    def __init__(self):
        self.con=sqlite3.connect("kütüphane.db")
        self.cursor= self.con.cursor()
        sorgu="CREATE TABLE IF NOT EXISTS kitaplar ('Kitapadi TEXT','yazar TEXT','Yayınevi TEXT','Tur TEXT','Baski INT')"
        self.cursor.execute(sorgu)
        self.con.commit()
    def listeleme(self):
        self.cursor.execute("select * from kitaplar")
        kitaplar=self.cursor.fetchall()

        for i in kitaplar:
            ver=Kitap(i[0],i[1],i[2],i[3],i[4])
            print(ver)

    def yayin_evi_degistir(self,eski,yeni):
        sorgu="Update kitaplar set Yayınevi  = ? where Yayınevi  = ? "
        self.cursor.execute(sorgu,(yeni,eski))
        self.con.commit()
        print("Yayın Evi yenileniyor bekleyiniz")
        time.sleep(1)

    def kitap_ekle(self,kitap):
        sorgu="Insert into kitaplar values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.kitapadi,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.con.commit()
    def kitap_sil(self,adi):
        sorgu="delete from kitaplar  where kitapadi = ? "
        self.cursor.execute(sorgu,(adi))
        self.con.commit()
    def baski_ekle(self,adi):
        sorgu="selecet * from kitaplar where kitapadi = ? "
        self.cursor.execute(sorgu,(adi,))
        kitaplar = self.cursor.fetchall()
        baski_sayısı= kitaplar[0][4]
        baski_sayısı+=1
        sorgu2="update kitaplar set baski = ? where kitapadi=?"
        self.cursor.execute(sorgu,(baski_sayısı,adi))
        self.con.commit()
    def sorgula(self,adi):
        sorgu="select kitaplar from where Kitapadi =?"
        self.cursor.execute(sorgu,(adi,))
        kitaplar= Kitap(self.cursor.fetchall())
        kitap_sorgu=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
        print(kitap_sorgu)










while True:
    deger= input("""
    * * * * *
    
    Çıkış için q ya
    Listeleme için 1 e
    Yayın evi değiştirmek için 2 ye
    kitap eklemek için 3 e
    kitap silmek için 4 e
    baskı arttırmak için 5 e
    kitap aramak için 6 ya Basınız....
    
    * * * * *
    """)
    if deger=="q":
        break
    elif deger=="1":
        Kutuphane().listeleme()
    elif deger=="2":
        eski=input("Eski Yayın evi  : ")
        yeni=input("Yeni yayın evi  : ")
        Kutuphane().yayin_evi_degistir(eski,yeni)
        print("Bekleyiniz...")
        time.sleep(1)
        print("Yayınevi Başarı ile değişitirldi")
    elif deger=="3":
        kitapadi=input("Adı :")
        yazar=input("Yazarı :")
        yayinevi=input("Yayınevi :")
        tur=input("Türü : ")
        baski=int(input("Baskısı  :"))
        kayit_kitabi =Kitap(kitapadi,yazar,yayinevi,tur,baski)
        Kutuphane().kitap_ekle(kayit_kitabi)
        print("Kitap başaroı ile eklendi")
    elif deger=="4":
        adi=input("Kitap Adını Giriniz : ")
        Kutuphane().kitap_sil(adi)
        print("kitap başarı ile silindi")
    elif deger=="5":
        adi = input("Kitap Adını Giriniz : ")
        Kutuphane().baski_ekle(adi)
        print("Baskı sayısı arttı")
    elif deger=="6":
        adi = input("Kitap Adını Giriniz : ")
        Kutuphane().sorgula(adi)
        print("başarılı")
    else:
        print("HATALI İŞLEMM")