# import library
import random

# pilihan user
print("Selamat Bermain")
print("1.Gunting")
print("2.Batu")
print("3.Kertas")
user = int(input("Masukan 1-3:"))

# menangkap pilihan comp 1
comp = random.randint(1,3)

# pilihan com
if comp == 1:
    computer = 'Gunting'
elif comp == 2:
    computer = 'Batu'
elif comp == 3:
    computer = "Kertas"

if user == 1:
    orang = 'Gunting'
elif user == 2:
    orang = 'Batu'
elif user == 3:
    orang = "Kertas"

print(f"Kamu Memilih {orang} dan Komputer {computer}")
# menentukan hasil

if user == comp:
    hasil = "Seri"
    menang = "Tidak ada yang menang"
    print(hasil)
    print(menang)
elif ((user == 1) and (comp == 2)) or ((user == 2) and (comp == 3)) or ((user == 3) and (comp == 1)):
    hasil = "Kalah"
    menang = 'dimenangkan oleh comp'
    print(f"Kamu {hasil}")
    print(f"pertandingan ini {menang}")
elif ((user == 1) and (comp == 3))  or ((user == 2) and (comp == 1)) or ((user == 3) and (comp == 2)):
    hasil = "Menang"
    menang = f'dimenangkan oleh Kamu'
    print(f"Kamu {hasil}")
    print(f"pertandingan ini {menang}")
else:
    print('Input Salah')
