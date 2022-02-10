class Insan():
    def __init__(self, ad, soyad, yas, ulke, sehir, yetenekler):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = yetenekler

    def kisi_bilgileri(self, index):
        return "{}. {} {}, {}, {} - {}, Yetenekler :{} ".format(
            index,
            self.ad,
            self.soyad,
            self.yas,
            self.ulke,
            self.sehir,
            self.yetenekler)

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)

print("\nUygulamayı çalıştırmak için en az 1 yetenek eklemelisiiniz!\n")

yetenekler = []
isnext = "e"
while isnext == "e":
    yetenek = input("Yetenek giriniz :")
    yetenekler.append(yetenek)
    isnext = input("Yetenek eklemek için e ye basınız :")
print(yetenekler)

print("\nUygulamayı çalıştırmak için en az 1 insan eklemelisiiniz!\n")
insanlar = []
isnext = "e"
while isnext == "e":
    ad = input("Ad Giriniz :")
    soyad = input("Soyad Giriniz :")
    yas = input("Yaş Giriniz :")
    ulke = input("Ülke Giriniz :")
    sehir = input("Şehir Giriniz :")
    insan = Insan(ad, soyad, yas, ulke, sehir, [])

    insanlar.append(insan)
    isnext = input("\nBaşka İnsan eklemek için e'ye basın :")

print("\nSistemdeki Kişi Listesi")
index =0
for x in insanlar:
  print(x.kisi_bilgileri(index + 1))
  index = index+1

print("\nYetenek eklemek istediğiniz kişinin sıra numarasını giriniz: ")
isnext = "e"
while isnext == "e":
    siraNo = int(input("Sıra No: "))
    if 0< siraNo <= len(insanlar):
        insan = insanlar[siraNo - 1]
        yetenekIndex = 1
        print("\nEkleyebileceğiniz Yetenekler :")
        for x in yetenekler:
            print("{}. {}".format(yetenekIndex, x))
            yetenekIndex = yetenekIndex + 1
        yetenekNo = int(input("\nEklemek istediğiniz yetenek Numarasını giriniz : "))
        if 0 < yetenekNo <= len(yetenekler):
            yetenek = yetenekler[yetenekNo-1]
            insan.yetenek_ekle(yetenek)
        isnext = input("Başka İnsana yetenek eklemek için e'ye basın :")
        print(insan.kisi_bilgileri(siraNo))
    else:
        print("Lütfen geçerli sıra numarası giriniz :\n")