import random
import time

class Kumanda():

    def __init__(self,tv_durumu = "Kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "Trt" ):
        
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durumu == "Açık"):
            print("Televizyon Zaten Açık")
        
        else:
            print("Televizyon Açılıyor")
            self.tv_durumu = "Açık"

    def tv_kapat(self):
        
        if (self.tv_durumu == "Kapalı"):
             print("Televizyon Zaten Kapalı")

        else:
             print("Televizyon Kapanıyor")
             self.tv_durumu = "Kapalı"

    def ses_ayarla(self):

        while True:
            cevap = input("\nSesi Arttırmak İçin: '>'\nSesi Azaltmak İçin: '<'\nÇıkmak İçin Herhangi Bir Tuşa Basın:")
            if (cevap == ">"):
                if(self.tv_ses!=32):

                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)

            elif (cevap == "<"):
                if(self.tv_ses!=0):

                    self.tv_ses-=1
                    print("Ses",self.tv_ses)

            else:
                print("Ses Güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):

        print("Kanal Ekleniyor..")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanallar Eklendi")

    def kanal_sil(self,silinecek_kanal):
        
        print("Kanal Siliniyor..")
        time.sleep(1)
        
        self.kanal_listesi.remove(silinecek_kanal)

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu Anki Kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()
print(""" Kumanda Uygulamasına Hoşgeldiniz

1. Tv Aç

2. Tv Kapa

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sil

6. Kanal Sayısını Öğren

7. Rastgele Kanala Geçme

8. Televizyon Bilgileri

Çıkmak İçin q'ya Basın
""")

while True:

    işlem = input("\nİşlem Seçiniz:")

    if (işlem=="q"):
        print("Program Sonlandırılıyor..")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarla()

    elif (işlem == "4"):
        kanal_isimleri = input("Lütfen Ekleyeceğiz Kanalları ',' Kullanarak Girin:")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    
    
    elif (işlem == "5"):
        silinecek = input("Lütfen Sileceğiniz Kanalı Girin")
        kumanda.kanal_sil(silinecek)          

    elif (işlem == "6"):
        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "7"):
        kumanda.rastgele_kanal()

    elif (işlem == "8"):
        print(kumanda)

    else:
        print("Geçersiz İşlem...")




        

       

        


    
