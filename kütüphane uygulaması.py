import os
kitapliste = list()

menü ="""
[1]KİTAP EKLE
[2]KİTAP AL
[3]KİTAPLARI LİSTELE
[Q]ÇIKIŞ
"""
def kitapekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Kitap Eklendi...")
    print("Ana menü'ye dönmek için Enter'e basın!")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True

    else:
        return False

def kitapçıkar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap Çıkarıldı...")
        print("Ana menü'ye dönmek için Enter'e basın!")
        input()
    else:
        print("Arattığınız kitap mevcut değil.")
        print("Ana menü'ye dönmek için Enter'e basın!")
        input()

def kitaplistele(liste:list):
    for i in liste:
        print("Kitap Adı: {} ========>>>>>>> Kitap Yazarı: {}".format(i[0],i[1]))




while True:
    os.system("clear")
    print(menü)

    seçim = input("İşleminizi Seçiniz:")

    if seçim == "1":
        kitap_isim = input("Kitab'ın adı ========>>>>>>>")
        kitap_yazar = input("Kitab'ın yazarı ========>>>>>>>")
        kitap = (kitap_isim,kitap_yazar)
        kitapekle(kitap,kitapliste)

    elif seçim == "2":
        kitap_isim = input("Kitab'ın adı ========>>>>>>>")
        kitap_yazar = input("Kitab'ın yazarı ========>>>>>>>")
        kitap = (kitap_isim, kitap_yazar)
        kitapçıkar(kitap,kitapliste)

    elif seçim == "3":
        kitaplistele(kitapliste)

    elif seçim == "q" or seçim == "Q":
        print("Çıkış Yapılıyor...")
        quit()

    else:
        print("Hatalı girdiniz!!!")



