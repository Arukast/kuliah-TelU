"""
=== Soal 1 ===
**Judul Masalah: Penghitungan Hewan di Peternakan**

**Deskripsi:**

Pak Budi memiliki sebuah peternakan yang luas di desa Sukamaju. Di peternakan tersebut, ia memelihara ayam, kambing, dan sapi. Setiap hari, ia melakukan pengecekan jumlah hewan-hewan tersebut untuk memastikan semuanya dalam keadaan baik. Namun, karena kesibukannya, Pak Budi kesulitan untuk menghitung jumlah total kaki hewan di peternakannya setiap hari. Bantulah Pak Budi untuk membuat program yang dapat menghitung jumlah total kaki dari semua hewan yang ada di peternakannya.

**Input:**

Program menerima tiga angka bulat positif yang dipisahkan oleh spasi, masing-masing mewakili jumlah ayam, kambing, dan sapi yang ada di peternakan Pak Budi.

**Output:**

Program harus mengeluarkan satu angka bulat yang merupakan jumlah total kaki dari semua hewan di peternakan.
Contoh Input:
5 3 2

Contoh Output:
30

**Penjelasan:**

Pak Budi memiliki 5 ayam, 3 kambing, dan 2 sapi di peternakannya. Diketahui setiap ayam memiliki 2 kaki, kambing memiliki 4 kaki, dan sapi juga memiliki 4 kaki. Maka, jumlah total kaki hewan di peternakan adalah (5 * 2) + (3 * 4) + (2 * 4) = 10 + 12 + 8 = 30.

**Batasan:**

**Petunjuk:**

1. Gunakan tipe data yang tepat untuk menyimpan jumlah ayam, kambing, dan sapi.
2. Hitung jumlah total kaki dengan mengalikan jumlah hewan dengan jumlah kaki masing-masing hewan, lalu tambahkan semua hasil perhitungan tersebut.
"""
def soal1():
    print('--- Soal 1 ----')
    ayam, kambing, sapi = [int(x) for x in input().split()]
    jumlah_kaki = ((ayam * 2)+(kambing * 4)+(sapi * 4))
    print(jumlah_kaki)


"""
=== Soal 2 ===
**Judul Masalah: Distribusi Pakan di Peternakan**

**Deskripsi:**

Pak Budi mengelola sebuah peternakan yang besar di desa Sukamaju. Di peternakan tersebut, ia memelihara ayam, kambing, dan sapi. Setiap jenis hewan membutuhkan jumlah pakan yang berbeda setiap harinya: setiap ayam membutuhkan 0.5 kg pakan, setiap kambing membutuhkan 3.5 kg pakan, dan setiap sapi membutuhkan 5 kg pakan. Pak Budi menghadapi tantangan dalam menghitung total berat pakan yang diperlukan untuk semua hewan dalam satu hari. Buatlah program yang dapat membantu Pak Budi menghitung total berat pakan yang dibutuhkan.

**Input:**

Input terdiri dari tiga baris:

- Baris pertama berisi satu bilangan bulat positif `N`, jumlah hari untuk distribusi pakan.
- Baris kedua berisi tiga bilangan bulat positif `A`, `K`, dan `S`, masing-masing mewakili jumlah ayam, kambing, dan sapi di peternakan Pak Budi.
- Baris ketiga hingga `N+2` berisi tiga bilangan bulat `a`, `b`, dan `c` untuk setiap hari, yang mewakili penambahan atau pengurangan jumlah ayam, kambing, dan sapi pada hari tersebut. Jika angka negatif, berarti ada pengurangan jumlah hewan, dan jika positif, berarti ada penambahan.

**Output:**

Program harus mengeluarkan satu bilangan real yang merupakan total berat pakan yang diperlukan untuk `N` hari, dibulatkan ke dua angka desimal.

contoh Input:
2
5 3 2
1 1 -1
-1 -2 0

Contoh Output:
36.50

**Penjelasan:**

Pada hari pertama, ada penambahan 1 ayam, 1 kambing, dan pengurangan 1 sapi, sehingga menjadi 6 ayam, 4 kambing, dan 1 sapi. Kebutuhan pakan pada hari kedua adalah (6 * 0.5) + (4 * 3.5) + (1 * 5) = 3 + 14 + 5 = 22 kg. Pada hari kedua, ada pengurangan 1 ayam dan 2 kambing, sehingga mempengaruhi kebutuhan pakan hari itu. Total pakan untuk dua hari adalah 22+14.5 = 36.5 kg.

**Petunjuk:**

1. Simpan jumlah hewan di awal dan perbarui jumlah tersebut setiap hari berdasarkan input.
2. Hitung kebutuhan pakan setiap hari berdasarkan jumlah hewan yang ada pada hari itu.
3. Gunakan tipe data yang sesuai untuk menyimpan nilai real dan memastikan hasil akhir dibulatkan ke dua angka desimal.
"""

def soal2():
    print('--- Soal 2 ----')
    hari = int(input())
    ayam, kambing, sapi = [int(x) for x in input().split()]
    pakan = 0
    while hari > 0:
        ayam1, kambing1, sapi1 = [int(x) for x in input().split()]
        ayam += ayam1 
        kambing += kambing1 
        sapi += sapi1 
        pakan += ((ayam * 0.5)+(kambing * 3.5)+(sapi * 5))
        hari -= 1
    print(f"{pakan:.2f}")

"""
=== Soal 3 ===
**Judul Masalah: Pemilihan Kursi di Bioskop**

**Deskripsi:**

Di sebuah bioskop, terdapat sebuah ruangan dengan baris kursi yang disusun dalam satu baris dari 1 hingga N. Kursi-kursi ini dapat berstatus terisi ('T') atau kosong ('K'). Seorang penonton ingin memilih sebuah kursi sedemikian rupa sehingga ia bisa duduk sejauh mungkin dari penonton lain untuk menjaga privasi dan kenyamanan, tetapi jika ada lebih dari satu pilihan, dia akan memilih kursi dengan nomor terkecil. Anda perlu membantu penonton tersebut menentukan nomor kursi yang harus dipilih.

**Input:**

- Baris pertama berisi satu bilangan bulat positif N , jumlah kursi dalam baris tersebut.
- Baris kedua berisi sebuah string S berpanjang N karakter, di mana setiap karakter mewakili status kursi ('T' untuk terisi dan 'K' untuk kosong).

**Output:**

- Sebuah bilangan bulat yang mewakili nomor kursi yang harus dipilih. Jika tidak ada kursi kosong, cetak "Penuh".

Contoh Input 1:
5
KTKKK

Contoh Output 1:
5

Contoh Input 2:
4
TTTT

Contoh Output 2:
Penuh

Contoh Input 3:
6
KTKKTK

Contoh Output 3:
1

**Penjelasan:**

- Pada Contoh 1, kursi nomor 5 adalah pilihan terbaik karena menjaga jarak maksimal dari penonton lain (kursi nomor 2 terisi).
- Pada Contoh 2, tidak ada kursi kosong, jadi outputnya adalah "Penuh".
- Pada Contoh 3, dipilih nomor terkecil

**Batasan:**

- Dalam penyelesaian masalah ini, Anda diperbolehkan menggunakan struktur kontrol dasar seperti perulangan (for, while) dan kondisional (if-else).

**Petunjuk:**

1. Anda dapat mengiterasi setiap karakter dalam string untuk mengecek kursi yang kosong.
2. Hitung jarak dari setiap kursi kosong ke kursi terisi terdekat untuk menemukan kursi dengan jarak maksimal.
3. Jika terdapat lebih dari satu kursi dengan jarak maksimal yang sama, pilih kursi dengan nomor terkecil.
"""
def soal3():
    print('--- Soal 3 ----')
    jml_kursi = int(input())
    kursi = input()
    op = []
    jarak_maks = 0
    kursi_terbaik = 0
    for z in kursi.upper():
        if z == 'K':
            op.append(1)
        else:
            op.append(0)
    if sum(op) == 0:
        print('Penuh')
    else:
        for i in range(jml_kursi):
            if op[i] == 1:
                kursi_terdekat = None
                for j in range(len(op)):
                    if op[j] == 0:
                        jarak = abs(i - j)
                        if kursi_terdekat == None or kursi_terdekat < jarak:
                            kursi_terdekat = jarak
                        else:
                            pass
                    else:
                        pass
                if kursi_terdekat is not None and jarak_maks < kursi_terdekat:
                    jarak_maks = kursi_terdekat
                    kursi_terbaik = i
                else:
                    pass
            else:
                pass
        print(kursi_terbaik+1)

"""Pemanggilan Fungsi"""
# soal1()
# soal2()
soal3()