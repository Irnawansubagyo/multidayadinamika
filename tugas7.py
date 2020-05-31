#7. Buatlah program untuk membalikkan "semua kata-kata" yang terdapat dalam kalimat.
def balikkata (kalimat):
    return ' '.join(kata(::-1) for kata in kalimat.split())

while True:
    kalimat = raw_input('Kata/Kalimat: ')
    if kalimat== "exit":
        break
hasil = balikkata(kalimat)
print hasil