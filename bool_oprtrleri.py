#and
#or
#not 

sayi = int(input("sayı giriniz:"))

if sayi > 5 and sayi %2 == 0:
	print("doğru")
#burada and mantıksal kapı olarak kullanılmış ve karmaşıklığı önlemiş.burada denmek istenen "eğer sayı yani alıcının yazdığı sayı 
#5'den büyükse ve iki ile bölümden kalan sıfırsa ekrana doğru" yazdır demektedir.Buradaki amaç and operatorunu anlamaktır.

x = int(input("x giriniz:"))

y = int(input("y giriniz:"))

if x == 5 or y == 5:
	print("doğru")

else:
	print("'x' veya 'y' 5 olmalı")
#Burada denmek istenen "eğer x 5 ise veya y 5 ise ekrana dogru yaz değilse ekrana x veya y 5 olmalı yaz demektedir.Buradaki x ve y
#alıcının yazdığı sayıdır."

z = (input("bir şey giriniz:"))
c = (input("bir şey giriniz:"))

if not bool(z):
	print("Doğru!")
#Burada "not" kelimesinin ne işe yaradığını öğrendik not kelimesi doğru olan birşseyi yanlış yada yanlış olan birşeyi doğruya cevirir.
#yani birşeyin tam tersini  yapmaktadır.Burada bool yazıyor ve boolda boşluk olduğu zaman false olarak geçiyordu ama not kelimesi 
#sayesinde true olarak geçiyor.
