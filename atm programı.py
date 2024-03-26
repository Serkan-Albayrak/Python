print("""***********************

Atm Makinesine Hoşgeldiniz.

İşlemler:
      
1.Bakiye Sorgulama
      
2.Para Yatırma
      
3.Para Çekme

Programda çıkmak için 'q' ya basın.

*******************************""")


money = 1000 

while True:
    process = input("İşlemi seçiniz: ")

    if (process == "q"):
        print("Yine Bekleriz: ")
        break
    elif (process == "1"):
        print("Bakiyeniz {} tl dir ".format(money))
    elif (process == "2"):
        amount = int(input("Miktarı giriniz: "))
        money += amount
    elif (process == "3"):
        amount = int(input("Miktarı giriniz: "))
        if (money - amount < 0):
            print("Böyle bir miktarı çekemezsiniz.")
            continue
        money -= amount
    else:
        print("Geçersiz İşlem ")






