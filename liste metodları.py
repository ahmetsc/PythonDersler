kitaplar = ["ince memed","ruby","qwert","denizci"]

kitaplar.append("naber delikanlı")
kitaplar.remove("qwert")
kitaplar.append("denizci")

def listele(kitaplar):
    for a in kitaplar:
        print(a)
listele(kitaplar)

print(kitaplar.count("denizci"))
#".count" saymaya yarar.

a = ["ruby","python","C++","Java","C"]
b = [3,5,4,8,9,0,2,6,1,7,10]
a.sort()
b.sort()
print(a,"\n",b)
#Alfabetik sıraya göre ekrana yazdırılacaktır.
