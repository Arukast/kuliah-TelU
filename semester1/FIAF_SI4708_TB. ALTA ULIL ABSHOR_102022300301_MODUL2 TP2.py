print("=== Tugas Pendahuluan No.1 ===")
"""1. Matthew adalah seorang kakak yang baik dan sedang membantu adiknya yang
berada di kelas 2 SD untuk memahami konsep bilangan ganjil dan genap. Dia
sedang membuat program Python sederhana yang dapat membantu adiknya
membedakan bilangan ganjil dan genap.
Berikut adalah contoh keluaran yang diharapkan:
• Jika Matthew memasukkan angka 7, maka program akan menghasilkan output
"Angka 7 adalah bilangan Ganjil!"
• Jika Matthew memasukkan angka 14, maka program akan menghasilkan output
"Angka 14 adalah bilangan Genap!”
Tugas Anda adalah membuat program Python sesuai dengan deskripsi di atas."""

x1 = int(input("Masukan angka Anda: "))
x2 = x1 % 2
if x2 == 0:
    print(f"Angka {x1} adalah bilangan Genap!")
else:
    print(f"Angka {x1} adalah bilangan Ganjil!")

print("=== Tugas Pendahuluan No.2 ===")
"""2. William membuat sebuah program untuk mengetahui nilai indeks huruf
mahasiswa, dengan ketentuan sebagai berikut :
Nilai 80 sampai dengan 100 maka mendapatkan indeks “A”
Nilai 70 sampai dengan 79 maka mendapatkan indeks ”AB”
Nilai 60 sampai dengan 69 maka mendapatkan indeks “B”
Nilai 50 sampai dengan 59 maka mendapatkan indeks “BC”
Nilai 40 sampai dengan 49 maka mendapatkan indeks “C”
Nilai 30 sampai dengan 39 maka mendapatkan indeks “D”
Nilai 0 sampai dengan 29 maka mendapatkan indeks “E”
Nilai LEBIH DARI 100 DAN KURANG DARI 0 “NILAI DILUAR JANGKAUAN”
Contoh : William memasukkan nilai 62 maka output programnya adalah AB
Tugas Anda adalah membuat program Python sesuai dengan deskripsi di atas."""

nilai = int(input("Masukan nilai Anda: "))
if nilai >= 80 and nilai <= 100:
    print("A")
elif nilai >= 70 and nilai <= 79:
    print("AB")
elif nilai >= 60 and nilai <= 69:
    print("B")
elif nilai >= 50 and nilai <= 59:
    print("BC")
elif nilai >= 40 and nilai <= 49:
    print("C")
elif nilai >= 30 and nilai <= 39:
    print("D")
elif nilai >= 0 and nilai <= 29:
    print("E")
else:
    print("NILAI DILUAR JANGKAUAN")
