import time
while True:
    print("İşlemden çıkmak isterseniz lütfen 'e'ye basın! ")
    x=input("Lütfen ilk sayıyı giriniz:")
    if x == "e":
        print("İşlemden çıkılıyor...")
        timet=time.sleep(2)
        break
    y=input("Lütfen ikinci sayıyı giriniz:")
    if y == "e":
        print("İşlemden çıkılıyor...")
        timet=time.sleep(2)
        break
    z=input("İşlem işareti (+,-,*,/)")
    if z == "e":
        print("İşlemden çıkılıyor...")
        timet=time.sleep(2)
        break
    c=0
    if z == ("+"):
        x=int(x)
        y=int(y)
        c=int(x+y)
        print(f"Toplama işlemi sonucunuz {c}'dir")
        continue
    elif z == ("-"):
        x=int(x)
        y=int(y)
        c=int(x-y)
        print(f"Çıkarma işlemi sonucunuz {c}'dir")
        continue
    elif z == ("/"):
        x=int(x)
        y=int(y)
        c=x/y
        print(f"Bölme işlemi sonucunuz {c}'dir")
        continue
    elif z == ("*"):
        x=int(x)
        y=int(y)
        c=int(x*y)
        print(f"Çarpma işlemi sonucunuz {c}'dir")
        continue
    else:
        print("Lütfen geçerli bir işlem veya sayı girin!")
        continue
    
    
    