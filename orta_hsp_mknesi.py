print("""
[1]TOPLAMA
[2]ÇIKARMA
[3]ÇARPMA
[4]BÖLME
[5]ÜS ALMA
[Q]ÇIKIŞ
	""")

giriş = input("Lütfen Yukarıdan işlem seçiniz:")

if giriş == "1":
	x = input("Birinci sayıyı giriniz:")
	x = float(x)
	y = input("İkinci sayıyı giriniz:")
	y = float(y)
	print("========================")
	print("İşlem sonucunuz:",x + y)
	print("========================")

elif giriş == "2":
	x = input("Birinci sayıyı giriniz:")
	x = float(x)
	y = input("İkinci sayıyı giriniz:")
	y = float(y)
	print("========================")
	print("İşlem sonucunuz:",x - y)
	print("========================")

elif giriş == "3":
	x = input("Birinci sayıyı giriniz:")
	x = float(x)
	y = input("İkinci sayıyı giriniz:")
	y = float(y)
	print("========================")
	print("İşlem sonucunuz:",x * y)
	print("========================")

elif giriş == "4":
	x = input("Birinci sayıyı giriniz:")
	x = float(x)
	y = input("İkinci sayıyı giriniz:")
	y = float(y)
	print("========================")
	print("İşlem sonucunuz:",x / y)
	print("========================")

elif giriş == "5":
	x = input("Taban sayını giriniz:")
	x = float(x)
	y = input("Üs sayısını giriniz:")
	y = float(y)
	print("========================")
	print("İşlem sonucunuz:",x ** y)
	print("========================")

elif giriş == "q" or "Q":
	print("Çıkış yaptınız.........")
	quit()

else:
	print("Hatalı girdiniz!")
	quit()

if giriş == "q" or "Q":
	print("Çıkış yapılıyor.........")
	quit()	


