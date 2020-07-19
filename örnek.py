urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i = 0

while(i<adet):
    name = input('ürün ismi: ')
    price = float(input('ürün fiyatı: '))
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} =======>>>>>>> ürün fiyatı: {urun["price"]}')