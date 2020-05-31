#1 .Buatlah program yang dapat menentukan grade dari suatu masukan angka, dengan kriteria sebagai berikut:

#Jika angka lebih besar atau sama dengan 90, maka output adalah huruf A
#Jika angka di antara 80 dan 89, maka output adalah huruf B
#Jika angka di antara 70 dan 79, maka output adalah huruf C
#Jika angka di antara 60 dan 69, maka output adalah huruf D
#Jika angka lebih kecil dari pada 59, maka output adalah huruf E

nilai = 99;

if nilai >= 90:
    print("Angka anda adalah A") :
elif 80 <= nilai <= 89:
    print("Angka anda adalah B"):
elif 70 <= nilai <= 79:
    print("Angka anda adalah C"):
elif 60 <= nilai <= 69:
    print("Angka anda adalah D")
elif nilai < 60:
    print("Angka anda adalah E")
else :
    print("Maaf Anda Tidak Terdata")