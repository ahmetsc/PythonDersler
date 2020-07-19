process = input("""
^===================^
^[1] TOPLAMA İŞLEMİ ^
^===================^
^[2] ÇIKARMA İŞLEMİ ^
^===================^
^[3] ÇARPMA İŞLEMİ  ^
^===================^
^[4] BÖLME İŞLEMİ   ^ 
^===================^
\nProcess Number Write: """)
if process == "1":
    x = input("First Number: ")
    y = input("Second Number: ")
    print("Total: ", x, '+', y, '=', float(x) + float(y))
elif process == "2":
    x = input("First Number: ")
    y = input("Second Number: ")
    print("Total: ", x, '-', y, '=', float(x) - float(y))
elif process == "3":
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Total: ", x, '*', y, '=', float(x) * float(y))
elif process == "4":
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Total: ", x, '/', y, '=', float(x) / float(y))
else:
    print("HATALI TUŞLAMA YAPTINIZ...")



