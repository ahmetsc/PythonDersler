x = input("parola'yı yazınız:")

şifre = "deneme"

if x !=  şifre:
	print("Parola yanlış")
#Buradaki "==" işareti eşitse,doğruysa anlamına gelmektedir.Fakat "!=" bu işaret eşit değilse, doğru değilse anlamına gelmektedir.
#Yukarıdaki kısımda eğer x yani alıcı parolayı doğru yazmadıysa ekrana parola yanlış diye çıktı yazdır demektedir.

y = input("10 ile 100 arasında bir sayı giriniz:")

y = int(y)

if y > 50:
	print("Sayı 50'den büyüktür.")
#Burada '>' işareti büyüktür anlama gelmektedir.yai burada denmek istenen eğer y 50 den büyükse ekrana sayı 50den büyüktür yaz demektedir.

if y < 50:
	print("Sayı 50'den küçüktür.")
#Burada '<' işareti küçüktür anlamına gelmektedir.burada denmek istenen eğer y 50 den küçükse ekrana sayı 50den küçüktür yaz demektedir.
else:
	print("Sayı 50'dir.")
#Burada denmek istenen sayı 50den küçük ve büyük değildir yani sayı 50 dir demek istiyor.
#birde küçük eşitse ve büyük eşitse işaretleri var bunlar şu şekilde gösterilir'<='bu küçük eşittir.'=>'bu ise büyük eşittir.