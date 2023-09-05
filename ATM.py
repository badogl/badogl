# Bank Account
# Hesap numarası depola
# Balance
# Hesaptaki miktar
# Hesap şifresi ve hesaplar arasındaki şifre uyumu
# Banka işlemleri (Ekleme,çıkarma ama bunu yaparken hesapdaki miktara dikkat etme)

import time

# Account number and passaport
Accountsandpasswords={"AccountNumber0": "1", "AccountPassaport0":"1","AccountBalance0":"1",
                      "AccountNumber1": "23312214", "AccountPassaport1":"1453","AccountBalance1":"1453",
                      "AccountNumber2": "39390303", "AccountPassaport2":"1461","AccountBalance2":"1461",
                      "AccountNumber3": "43834317", "AccountPassaport3":"1652", "AccountBalance3":"1652"}


# Account number and passaport short
AC0=[Accountsandpasswords["AccountNumber0"] , Accountsandpasswords["AccountPassaport0"],Accountsandpasswords["AccountBalance0"]]
AC1=[Accountsandpasswords["AccountNumber1"] , Accountsandpasswords["AccountPassaport1"],Accountsandpasswords["AccountBalance1"]]
AC2=[Accountsandpasswords["AccountNumber2"] , Accountsandpasswords["AccountPassaport2"],Accountsandpasswords["AccountBalance2"]]
AC3=[Accountsandpasswords["AccountNumber3"] , Accountsandpasswords["AccountPassaport3"],Accountsandpasswords["AccountBalance3"]]
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
            
            AC0[2]=int(AC0[2])
            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {AC0[2]}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                AC0[2]= AC0[2] + amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {AC0[2]}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > AC0[2]:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                AC0[2]= AC0[2] -amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {AC0[2]}!")
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
            
            AC1[2]=int(AC1[2])
            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {AC1[2]}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                AC1[2]= AC1[2] +amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {AC1[2]}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > AC1[2]:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                AC1[2]=AC1[2]-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {AC1[2]}!")
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
            
            AC2[1]=int(AC2[1])
            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {AC2[2]}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                AC2[2]= AC2[1] + amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {AC2[2]}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > AC2[2]:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                AC2[2]=AC2[2]-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {AC2[2]}!")
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
            
            AC3[0]= int(AC3[0])
            timet=time.sleep(3)
            print("\n""Hesap işlemleri""\n"
                "1- Hesap Özeti""\n"
                "2- Para Yatırma""\n"
                "3- Para Çekme""\n"
                "4- Çıkış (q) ""\n"
                "5- Ana ekran""\n")
            process=input()
            if process == "1":
                print(f"Güncel bakiyeniz {AC3[2]}$'dır.")
                continue
            elif process == "2":
                amountofadd=int(input("Yüklemek istediğiniz miktar: "))
                AC3[2]= AC3[0] +amountofadd
                timet=time.sleep(1)
                print(f"{amountofadd}$ yüklemeniz başarıyla sonuçlandı. Yeni bakiyeniz {AC3[2]}!")
                continue
            elif process == "3":
                amountofext=int(input("Çekmek istediğiniz miktar: "))
                if amountofext > AC3[2]:
                    print("Çekmek istediğiniz tutar bakiyenizden fazla...""\n"
                          "Lütfen tekrar deneyin!")
                    continue
                AC3[2]=AC3[2]-amountofext
                timet=time.sleep(1)
                    
                print(f"{amountofext}$ çekme işleminiz başarıyla sonuçlandı. Yeni bakiyeniz {AC3[2]}!")
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