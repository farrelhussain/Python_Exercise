angka = int(input("Masukan angka untuk menghitung Faktorial: "))
faktorial = 1

for i in range(1, angka+1):
    faktorial*= i

print("Faktorial dari ", angka, " Adalah: ",faktorial)