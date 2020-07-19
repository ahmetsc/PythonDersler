kitapliste = ["Bir Atın Hikayesi","Python","Linux Günlükleri","Dönüşüm"]

for i in kitapliste:
   print("Bu Kitab'ın Adı :" ,(i))

eklenecekk = input("Lütfen kitabın adını yazınız:")
kitapliste += [eklenecekk]
#Buradaki köşeli parantezin amacı kitapliste değişkeni gibi yazılması içindir.Eğer köşeli parantez konulmasaydı
#yazdıklarımızı harf harf ayıracaktı.
print(kitapliste)