kitap_listesi =[]

menü ="""
[1]KİTAP EKLE 
[2]KİTAP ÇIKAR
[3]KİTAPLARI LİSTELE
[4]ÇIKIŞ YAP(Q or q)
"""
def ekle(kitap,liste):
    liste += [kitap]
    print("kitap Eklendi.")
    input("Ana menüye dönmek için Enter'e basın.")

def çıkar():
    pass

def listele(liste):
    for i in liste:
        print("Kitab'ın Adı ========>>>>>> {}".format(i))

        input("Ana menüye dönmek için Enter'e basın.")

def çıkış():
    quit()

while True:
    print(menü)

    secim = input("Seçiminiz:")

    if secim == "1":
        kitapAdı = input("Kitap Adı :")
        ekle(kitapAdı,kitap_listesi)

    elif secim == "2":
        çıkar()

    elif secim == "3":
        listele(kitap_listesi)

    elif secim == "q" or secim == "Q":
        çıkış()

    else:
        print("Hatalı tuşladınız!!!")
        input("Ana menüye dönmek için Enter'e basınız.")

