degisken1 ="Ahmet"
degisken2 ="Taşçı"

ifade1 =("{1} {0}".format(degisken1,degisken2))
ifade2 =("{0} {1}".format(degisken2,degisken1))
#Süslü parantez içindeki sayılar değişken içindeki şeylerin yerlerini değiştiriyor python en ilk 0 dan başladığı için
#ifade1 taşçı ahmet ifade2 taşçı ahmet oluyor bunun sebebi en ilk sıfır okunup onu taşçı ve sonra 1 okunup ahmet yapıp
#taşçı ahmet yaptı ifade2de ise en ilk sıfır okunup ahmet yaptı sonra 1 okunup taşçı yaptı ve taşçı ahmet taşçı ahmet olarak ekrana yazdırdı.

print(ifade1)
print(ifade2)