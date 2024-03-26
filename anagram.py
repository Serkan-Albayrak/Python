def is_anagram():
    str1 = input("İlk Kelime").lower()
    str2 = input("İkinci Kelime").lower()
    if  sorted(str1)==sorted(str2):
       print(True)
    else:
       print(False)

is_anagram()