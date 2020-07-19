ilk_sayı = input("lütfen sayı giriniz:")
ikinci_sayı = input("lütfen ikinci bir sayı giriniz:")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/" ,sayı2, "=" ,sayı1 / sayı2)
except ValueError as hata:
    print(hata)
    print("Lütfen tekrar deneyin.")