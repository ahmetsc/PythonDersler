#in işleci aitlik işleidir

x ="123"

if "3" in x:
	print("Mevcut!")
else:
	print("Mevcut Değil!")
#Buradaki "in" şu anlama gelir;Eğer 3 sayısı x değişkeninin içinde varsa mevcut yaz yoksa yani değilse(else) mevcut değil yazn

giriş = input("lütfen parolanızı yazınız:")

if "_" not in  giriş:
	print("Alt çizgi veya nokta kullanmalısınız.")

else:
	print("Parola güvenli bir şekilde oluşturuldu.")
