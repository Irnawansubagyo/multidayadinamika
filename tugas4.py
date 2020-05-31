#4. Buatlah program untuk menentukan suatu kata atau kalimat merupakan palindrom atau bukan
kata = input("Masukan kata = ")
rev_kata = kata[::-1]
if kata == rev_kata:
    print("palindrom")
else :
    print("bukan palindrom")