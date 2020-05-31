#1 .Buatlah program yang dapat menentukan grade dari suatu masukan angka, dengan kriteria sebagai berikut:

#Jika angka lebih besar atau sama dengan 90, maka output adalah huruf A
#Jika angka di antara 80 dan 89, maka output adalah huruf B
#Jika angka di antara 70 dan 79, maka output adalah huruf C
#Jika angka di antara 60 dan 69, maka output adalah huruf D
#Jika angka lebih kecil dari pada 59, maka output adalah huruf E

#jawaban
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
    
#2. Buatlah program fungsi untuk menentukan suatu bilangan merupakan bilangan ganjil atau genap.
#jawaban

n =  int(input('masukan angka : '))
if %2 == 0 :
    print('Bilangan Genap')
else :
    print('Bilangan Gajil')
    
#3. Buatlah program untuk menentukan nilai maksimum, minimum, dan rata-rata dari suatu deretan angka.
#jawaban

def angkaMax(daftar):
    maksimal = 0
    for x in daftar:
        if x >  maksimal:
            maksimal=x
    return maksimal
def angkaMin(daftar_1):
    minimal = 999
    for y in daftar_1:
        if y < minimal:
            minimal=y
    return minimal

jumlahAngka =[]
angka=int(input(berapa banyak agka: ""))
for n in range(angka):
    inlai=int(input("masukan angka: "))
    jumlahAngka.append(nilai)
print("angka maksimum: "), angkaMax(jumlahAngka))

print("angka minimum"), angkaMin(jumlahAngka))

#lalu ini untuk mencari nilai rata-rata
n = eval(input("Masukan bilangan yang akan dihitung: "))
xn= float()
for x in range(n):
    x = x +1
    nilai = eval(input("Masukan nilai ke-%d:"%(x)))
    xn = xn + x
    avg = xn/n
print ("Hasil rata-rata adalah : %f"%(avg))

#4. Buatlah program untuk menentukan suatu kata atau kalimat merupakan palindrom atau bukan
#jawaban

kata = input("Masukan kata = ")
rev_kata = kata[::-1]
if kata == rev_kata:
    print("palindrom")
else :
    print("bukan palindrom")
    
#5. Buatlah program yang memiliki dua input berupa tahun. Output dari fungsi tersebut adalah list dari tahun-tahun kabisat diantara dua input tahun tersebut.
#jawaban

#6. Buatlah program rekursif. Anda bebas menentukan input dan output dari fungsi tersebut, tetapi harus rekursif.
#jawaban

def rekursif():
    abcdef
    
#7. Buatlah program untuk membalikkan "semua kata-kata" yang terdapat dalam kalimat.
#jawaban

def balikkata (kalimat):
    return ' '.join(kata(::-1) for kata in kalimat.split())

while True:
    kalimat = raw_input('Kata/Kalimat: ')
    if kalimat== "exit":
        break
hasil = balikkata(kalimat)
print hasil

#8
#9
#10
