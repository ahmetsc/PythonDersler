rehber = {
    "karakter1" : {"Ev Adresi" : "kaplan mahallesi çiçek caddesi 571. sokak no:13 daire:2",
                   "İş Adresi" : "bilmem caddesi 13.sokak no:17",
                   "Ev Telefonu" : "0548 658 7824"
    }
}
aranacak_kişi = input("Aranacak kişinin ismini yazınız :")
aranan_özellik = input("Bu kişi ile ne aramak istiyorsunuz :")
print(rehber.get(aranacak_kişi,"Böyle birisi bulunamadı."))

