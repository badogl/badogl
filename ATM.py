# Bank Account
# Hesap numarası depola
# Balance
# Hesaptaki miktar
# Hesap şifresi ve hesaplar arasındaki şifre uyumu
# Banka işlemleri (Ekleme,çıkarma ama bunu yaparken hesapdaki miktara dikkat etme)
# Kredi çekme işlemleri ve kredi yatırma işlemleri
# Ana girişe hesap açma butonu
import time

# Account number and passaport
Accountsandpasswords={"AccountNumber0": "1", "AccountPassaport0":"1",
                      "AccountNumber1": "23312214", "AccountPassaport1":"1453",
                      "AccountNumber2": "39390303", "AccountPassaport2":"1461",
                      "AccountNumber3": "43834317", "AccountPassaport3":"1652"}


# Account number and passaport short
AC0=[Accountsandpasswords["AccountNumber0"] , Accountsandpasswords["AccountPassaport0"]]
AC1=[Accountsandpasswords["AccountNumber1"] , Accountsandpasswords["AccountPassaport1"]]
AC2=[Accountsandpasswords["AccountNumber2"] , Accountsandpasswords["AccountPassaport2"]]
AC3=[Accountsandpasswords["AccountNumber3"] , Accountsandpasswords["AccountPassaport3"]]
# Balance
balance=0
# Bank Main Menu
while True:
    AccountNumber=input("Lütfen hesap numaranızı girin: ")
    AccountPassword=input("Lütfen şifrenizi girin: ")
    while True:  

        print("\n""Lütfen Yapmanız gereken işlemi girin...""\n")
        
        # Account 1
        if AccountNumber==AC0[0] and AccountPassword==AC0[1]:

            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {balance}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                balance=+amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > balance:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                balance=balance-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue   
            elif process == "q":
                print("İşlem bitiriliyor!")
                timet=time.sleep(1)
                break
            elif process == "b":
                print("Ana ekrana dönülüyor!")
                timet=time.sleep(1)
                continue 
            else:
                print(f"{process}'diye bir işlem yok,'\n'Lütfen geçerli bir işlem girin!")
                continue
        
        # Account 2
        elif AccountNumber==AC1[0] and AccountPassword==AC1[1]:

            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {balance}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                balance=+amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > balance:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                balance=balance-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue   
            elif process == "q":
                print("İşlem bitiriliyor!")
                timet=time.sleep(1)
                break
            elif process == "b":
                print("Ana ekrana dönülüyor!")
                timet=time.sleep(1)
                continue 
            else:
                print(f"{process}'diye bir işlem yok,'\n'Lütfen geçerli bir işlem girin!")
                continue
            
        # Account 3
        elif AccountNumber==AC2[0] and AccountPassword==AC2[1]:

            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {balance}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                balance=+amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > balance:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                balance=balance-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue   
            elif process == "q":
                print("İşlem bitiriliyor!")
                timet=time.sleep(1)
                break
            elif process == "b":
                print("Ana ekrana dönülüyor!")
                timet=time.sleep(1)
                continue 
            else:
                print(f"{process}'diye bir işlem yok,'\n'Lütfen geçerli bir işlem girin!")
                continue
        
        # Account 4
        elif AccountNumber==AC3[0] and AccountPassword==AC3[1]:

            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {balance}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                balance=+amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > balance:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                balance=balance-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {balance}!")
                continue   
            elif process == "q":
                print("İşlem bitiriliyor!")
                timet=time.sleep(1)
                break
            elif process == "b":
                print("Ana ekrana dönülüyor!")
                timet=time.sleep(1)
                continue 
            else:
                print(f"{process}'diye bir işlem yok,'\n'Lütfen geçerli bir işlem girin!")
                continue
        
        # Wrong
        else:
            print("Yanlış hesap numarası veya şifre !""\n"
                  "\n""Lütfen tekrar deneyiniz""\n")
            break