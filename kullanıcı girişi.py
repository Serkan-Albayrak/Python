print("""
***************************
Kullanıcı Girişi Programı
***************************
""")

sys_user_name= "serkan"
sys_password = "12345"
right = 3

while True:
    user_name = input("Kullanıcı adı: ")
    password = input("Parola giriniz: ")
    if (user_name != sys_user_name and password == sys_password):
        print("Kullanıcı adı hatalı.")
        right -= 1
    elif (user_name == sys_user_name and password != sys_password):
        print("Parola hatalı: ")
        right -= 1
    elif (user_name != sys_user_name and password != sys_password):
        print("Kullanıcı adı ve Parola hatalı: ")
        right -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı. ")
        break
    if (right == 0 ):
        print("Giriş hakkı bitti.")
        break


    