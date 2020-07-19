degisken ="Ahmet Taşçı"

ifade1 =("{:b}".format(1024))
ifade2 =("{:s}".format(degisken))
print(ifade1)
print((ifade2))

#burada denmek istenen 15 birim ismi sağa doğru yasla bunun işareti ise ':>' budur.
#':<' bu işaret ise sola dogru yasla demek
#ismi merkezde yapmak için ise şu işareti koymalıyız.':^'
#yalnızca string ifade için ise şu işareti yapmalıyız ':s' bu ifade yalnızca string ifadelerde geçerlidir.
#yalnızca sayısal ifade için ise şu işareti koymalıyız ':d' bu işaret yalnızca sayısal ifadelerde geçerlidir.
#ikili sistemdeki karşılık için isr şu işareti kullanmalıyız ':b'