
def sagslash(adet):
	for i in range(int(adet)):
		print("/" ,end="")


def solslash(adet):
	for i in range(int(adet)):
		print("\\" ,end ="")


def satıratlat(adet):
	for i in range(int(adet)):
		print()


def bosluk(adet):
	for i in range(int(adet)):
		print(" " ,end="")

def ustkisim(cap):
	baslangıcbosluk = cap/2-1
	for i in range(int(cap/2)):
		bosluk(baslangıcbosluk -i)
		sagslash(1)
		bosluk(1*2)
		solslash(1)
		satıratlat(1)


def altkısım(cap):
	baslangıcbosluk = cap-2
	for i in range(int(cap/2)):
		bosluk(i)
		solslash(1)
		bosluk(baslangıcbosluk - i*2)
		sagslash(1)
		satıratlat(1)


def paralelkenar(cap):
	ustkisim(cap)
	altkısım(cap)


paralelkenar(20)