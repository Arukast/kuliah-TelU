# Tugas Pendahuluan - No. 1
"""Pak Dengklek mempunyai ikan cupang sebanyak N. Ia ingin
membagikan koleksi ikan cupangnya kepada cucu-cucunya yang
berjumlah M. Ternyata, jumlah ikan cupang Pak Dengklek lebih
banyak daripada jumlah cucunya. Bantulah Pak Dengklek untuk
menentukan berapa ekor cupang yang harus dia berikan kepada
masing-masing cucunya, dan berapa sisanya."""

N = int(input("Masukan Jumlah cupang Pak Dengklek: "))
M = int(input("Masukan Jumlah cucu Pak Dengklek: "))
compute1 = int(N / M)
compute2 = int(N % M)
print(f"Masing-masing cucu  mendapatkan: {compute1} cupang")
print(f"Cupang Pak Dengklek tersisa: {compute2} ekor")

# Tugas Pendahuluan - No. 2
"""Pak Guts adalah seorang pengrajin senjata yang sangat suka
sekali membuat senjata di halaman belakang rumahnya. Suatu
hari, Pak Guts ingin membuat dua buah lingkaran yang berbeda
ukuran untuk alas dari senjatanya. Ketika mulai membuat kedua
lingkaran tersebut, Pak Guts kebingungan dan sadar bahwa dia
harus menghitung masing-masing luas lingkaran tersebut dan
membandingkan mana yang lebih besar. Bantulah Pak Guts untuk
membuat program yang dapat menghitung luas lingkaran dan
membandingkannya."""

N = float(input("Masukan jari-jari lingkaran yang pertama: "))
M = float(input("Masukan jari-jari lingkaran yang kedua: "))

L1 = float(3.14 * N * N)
L2 = float(3.14 * M * M)

print(f"Luas dari lingkaran pertama dan kedua adalah {L1} dan {L2}")

# Tugas Pendahuluan - No. 3
# Pak Luffy adalah seorang dosen yang memiliki banyak mahasiswa. Beliau memerintahkan kamu sebagai asistennya untuk membuat program menghitung nilai mahasiswanya. Pak Luffy memberitahumu bahwa nilai yang perlu dihitung dari mata kuliah yang diempunya adalah rata-rata dari nilai tugas, quiz, UTS, dan juga UAS milik masing-masing mahasiswa. Buatlah program untuk menghitung rata-rata nilainya dan inputan data diri mahasiswa untuk memudahkan kamu membantu Pak Luffy.

Tugas = int(input("Masukan nilai Tugas: "))
Quiz = int(input("Masukan nilai Quiz: "))
UTS = int(input("Masukan nilai UTS: "))
UAS = int(input("Masukan nilai UAS: "))
Nama = input("Nama : ")
NIM = input("NIM : ")
Kelas = input("Kelas : ")
rata = ((Tugas + Quiz + UTS + UAS) / 4)
print(
    f"Nilai MK Pengatar Pemrograman dan Logika milik {Nama} dengan NIM {NIM} Kelas {Kelas} adalah: {rata}")
