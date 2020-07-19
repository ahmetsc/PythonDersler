b = set()
a = {"dene","abcdfg","qwertyuıop"}
print(type(a),type(b))
#Burada denmek istenen b değişkeni birer kümedir.A değişkeninin küme olması şöyle o bir sözlük olmadığ için küme olarak sayılıyor
b.add("AHMET")
print(b)
#Burada b kümesine .add yazarak istediğimiz şeyi ekliyoruz.
a.discard("qwertyuıop")
print(a)
#Burada a kümesine .discard yazarak istediğimiz şeyi siliyoruz.
c = set([1,3,5])
d = set([3,4,5])
c.intersection(d)
print(c)
#Burada c kümesinin d kümesiyle kesişimleri .intersection ile bulunup ekrana yzdırılıyor