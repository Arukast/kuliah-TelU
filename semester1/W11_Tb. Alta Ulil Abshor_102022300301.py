# Nama: Tb. Alta Ulil Abshor
# NIM: 102022300301

print("=== Tugas Kuliah Asynchonous Sesi 11 ===")
# Pengatar Fungsi
print('--- Pengantar Fungsi ---')
print('Konsep Dasar dari Fungsi')
print('Function adalah sebuah blok kode yang dirancang untuk melakukan tugas tertentu, dan dapat dipanggil kembali di bagian lain dari program')
# Contoh sederhana fungsi
print('Contoh Sederhana Fungsi')

# Langkah-langkahnya adalah mendefinisikan setiap fungsi yang dibutuhkan lalu memanggilnya
# Tujuan dari fungsi menu_dosen adalah untuk menjalankan menu khusus untuk dosen


def menu_dosen():
    print('Selamat Datang di menu Dosen!')

# Tujuan dari fungsi menu_mahasiswa adalah untuk menjalankan menu khusus untuk mahasiswa


def menu_mahasiswa():
    print('Selamat Datang di menu Mahasiswa!')

# Tujuan dari fungsi main_contoh adalah sebagai fungsi pemanggil fungsi yang lain dan sebagai fungsi yang mengatur alur program


def main_contoh():
    print('Selamat Datang di menu Utama!')
    x_contoh = input('Apakah Anda seorang dosen?(Y/N): ').upper()
    if x_contoh == 'Y':
        menu_dosen()
    elif x_contoh == 'N':
        menu_mahasiswa()
    else:
        print('ERROR')


# disini dilakukan pemanggilan fungsi main_contoh
main_contoh()

# Deklarasi dan Pemanggilan Fungsi
print('--- Deklarasi dan Pemanggilan Fungsi ---')

# Langkah-langkahnya adalah mendefinisikan setiap fungsi yang dibutuhkan lalu memanggilnya
# Tujuan dari fungsi ini adalah untuk menerima dan mengkalkulasi dua parameter yang diberikan lalu mengembalikan hasil kalkulasinya


def fungsi_penjumlahan(bilangan1, bilangan2):
    hasil_penjumlahan = bilangan1 + bilangan2
    return hasil_penjumlahan

# Tujuan dari fungsi ini adalah sebagai fungsi yang mengatur alur program, meminta dua bilangan, memanggil fungsi_penjumlahan dengan memberikan dua parameter dari dua bilangan yang telah diminta, lalu menampilkan hasil akhir dari fungsi_penjumlahan


def main2():
    x1 = int(input('Masukan bilangan pertama: '))
    y1 = int(input('Masukan bilangan kedua: '))
    hasil_akhir = fungsi_penjumlahan(x1, y1)
    print(f'Hasil penjumlahan: {hasil_akhir}')


# Disini dilakukan pemanggilan fungsi main2
main2()

# Fungsi untuk menghitung Luas Segitiga
print('--- Fungsi untuk menghitung Luas Segitiga ---')
# Langkah-langkahnya adalah mendefinisikan setiap fungsi yang dibutuhkan lalu memanggilnya
# Tujuan dari fungsi ini adalah untuk mengkalkulasi luas segitiga dari dua parameter yang telah diberikan yaitu parameter alas dan tinggi lalu mengembalikan hasil kalkulasinya


def luas_segitiga(alas, tinggi):
    kalkulasi_segitiga = 0.5 * alas * tinggi
    return kalkulasi_segitiga

# Tujuan dari fungsi ini adalah sebagai fungsi yang mengatur alur program, meminta dua parameter yaitu panjang alas dan tinggi, memanggil fungsi luas_segitiga dengan memberikan dua parameter yang telah diminta, dan menampilkan hasil dari fungsi luas_segitiga


def main3():
    x2 = int(input('Masukan panjang alas segitiga: '))
    y2 = int(input('Masukan tinggi segitiga: '))
    hasil_segitiga = luas_segitiga(x2, y2)
    print(f'Luas segitia: {hasil_segitiga}')


# Disini dilakukan pemanggilan fungsi main3
main3()

# Fungsi untuk membuat program sederhana menghitung nilai rata-rata dari sejumlah angka yang dimasukkan pengguna
print('--- Fungsi untuk membuat program sederhana menghitung nilai rata-rata dari sejumlah angka yang dimasukkan pengguna ---')


# Langkah-langkahnya adalah mendefinisikan setiap fungsi yang dibutuhkan lalu memanggilnya
# Tujuan dari fungsi ini adalah untuk meminta pengguna memasukan jumlah nilai yang ingin dihitung dan kemudian meminta pengguna untuk memasukan nilai-nilai sesuai jumlah nilai yang ingin dimasukan, lalu fungsi akan mengembalikan nilai-nilai yang telah diminta
def input_nilai():
    x3 = int(input('Masukan jumlah angka yang ingin dimasukan: '))
    nilai = []
    for i in range(x3):
        nilai.append(int(input(f'Masukan nilai ke-{i + 1}: ')))
    return nilai

# Tujuan dari fungsi ini adalah untuk menghitung rata-rata dari parameter yang diberikan lalu mengembalikan hasil dari hitungannya


def hitung_rata_rata(nilai):
    rata_rata = sum(nilai) / len(nilai)
    return rata_rata

# Tujuan dari fungsi ini adalah sebagai fungsi yang mengatur alur program, memanggil fungsi input_nilai, memanggil fungsi hitung_rata_rata, dan menampilkan hasil dari fungsi hitung_rata_rata


def main():
    nilai = input_nilai()
    rata_rata_akhir = '{:.2f}'.format(hitung_rata_rata(nilai))
    print(
        f'Rata-rata dari sejumlah angka yang Anda masukan adalah: {rata_rata_akhir}')


# Disini dilakukan pemanggilan fungsi main dan pengecekan untuk memastikan bahwa fungsi akan berjalan jika dijalankan sebagai file utama, bukan diimpor sebagai modul
if __name__ == '__main__':
    main()
