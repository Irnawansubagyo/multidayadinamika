#3. Buatlah program untuk menentukan nilai maksimum, minimum, dan rata-rata dari suatu deretan angka.
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
