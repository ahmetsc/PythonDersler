sözlük = {"book":"kitap","pen":"kalem","eraser":"silgi"}

for i in sözlük.items():
    print(i)
#demet şeklinde yazdırır.

for i in sözlük.keys():
    print(i)
#Anahtar kelimeleri bastırır.Bizim anahtar kelimelerimiz ingilizce kelimeler

for i in sözlük.values():
    print(i)
#Değerleri ekrana bastırır.Bizim değer kelimelerimiz türkçe kelimeler

soru = input("yazınız:")
print(sözlük.get(soru,"Aratığınız kelime bulunumadı."))
