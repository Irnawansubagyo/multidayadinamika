n = eval(input("Masukan bilangan yang akan dihitung: "))
xn= float()
for x in range(n):
    x = x +1
    nilai = eval(input("Masukan nilai ke-%d:"%(x)))
    xn = xn + x
    avg = xn/n
print ("Hasil rata-rata adalah : %f"%(avg))

