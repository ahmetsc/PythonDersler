a = int(input("lütfen birinci kenarı yazınız: "))
b = int(input("lütfen ikinci kenarı yazınız: "))
c = int(input("lütfen üçüncü kenarı yazınız: "))

if a**2+b**2 == c**2:
	print("bu bir üçgendir.")
else:
	print("bu bir üçgen değildir.")