from array import array
from enum import Enum

"""1. udul Masalah: **Cari Tengah**

Deskripsi:

Ali berada dalam antrian pembelian tiket di sebuah bioskop dan ingin mencari tahu apakah ada orang yang tinggi badannya merupakan nilai tengah dari semua orang di antriannya. Setiap orang di antrian memiliki tinggi yang unik. Bantu Ali menemukan orang dengan tinggi badan nilai tengah tersebut!

Input:

- Baris pertama berisi satu bilangan bulat positif N , jumlah orang dalam antrian.
- Baris kedua berisi N bilangan bulat positif yang dipisahkan dengan spasi, masing-masing mewakili tinggi setiap orang dalam antrian (dalam centimeter).

Output:

- Sebuah bilangan bulat yang mewakili tinggi badan nilai tengah. Jika jumlah orang adalah genap, cetak nilai tengah yang lebih kecil.

Contoh Input 1:

5
150 160 145 155 140

Contoh Output 1:

150

Contoh Input 2:

4
170 160 150 180

Contoh Output 2:

160

Penjelasan:

- Pada Contoh 1, setelah mengurutkan tinggi badan menjadi 140, 145, 150, 155, 160, tinggi badan nilai tengah adalah 150.
- Pada Contoh 2, setelah mengurutkan tinggi badan menjadi 150, 160, 170, 180, karena jumlah orang genap, nilai tengah yang lebih kecil adalah 160.

Batasan:

- Dalam penyelesaian masalah ini, Anda diperbolehkan menggunakan fungsi pengurutan dan perhitungan statistik dasar.

Petunjuk:

1. Urutkan array yang berisi tinggi badan setiap orang.
2. Tentukan nilai tengah dari array yang sudah diurutkan. Jika jumlah elemennya genap, pilih elemen di posisi \(N/2\) setelah diurutkan (menggunakan indeks berbasis 0).

Masalah ini menguji pemahaman Anda tentang konsep pengurutan dan pencarian nilai tengah dalam array, serta pemahaman tentang indeksasi array yang berbasis 0."""


def soal1():
    var = array("i", [])
    n = int(input())
    for x in [int(x) for x in input().split()]:
        var.append(x)
    a = sorted(var)
    if n % 2 == 0:
        i = int(n / 2)
        print(a[i - 1])
    else:
        i = int((len(var)) / 2)
        print(a[i])
    # print(a[:])


"""1. Judul Masalah: **Rotasi Array**

Deskripsi:

Aria mempunyai sebuah kotak permen, dengan permen-permen tersebut diatur dalam sebuah array. Dia memiliki sebuah rutinitas unik dimana setiap hari, dia mengambil satu permen dari ujung kotak dan meletakkannya kembali di ujung lainnya, sehingga menciptakan pengaturan baru. Aria penasaran bagaimana tampilan akhir dari kotak permen tersebut setelah melakukan proses rotasi ini sebanyak k kali. Bantulah Aria menentukan susunan akhir dari kotak permen setelah k kali rotasi.

Input:

- Baris pertama berisi dua bilangan bulat positif, N dan k , di mana N adalah jumlah permen dalam kotak dan k adalah jumlah rotasi yang dilakukan.
- Baris kedua berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili tipe permen dalam kotak.

Output:

- N bilangan bulat yang dipisahkan dengan spasi, mewakili susunan akhir kotak permen setelah k kali rotasi.

Contoh Input 1:

5 2
1 2 3 4 5

Contoh Output 1:

4 5 1 2 3

Contoh Input 2:

4 3
9 8 7 6

Contoh Output 2:

8 7 6 9

Penjelasan:

- Pada Contoh 1, kotak permen [1, 2, 3, 4, 5] dirotasi sebanyak 2 kali. Rotasi pertama menghasilkan [5, 1, 2, 3, 4] dan rotasi kedua [4, 5, 1, 2, 3].
- Pada Contoh 2, kotak permen [9, 8, 7, 6] dirotasi sebanyak 3 kali, menghasilkan [8, 7, 6, 9].

Batasan:

- Dalam penyelesaian masalah ini, Anda diperbolehkan menggunakan struktur kontrol dasar dan operasi pada array."""


def soal2():
    var = array("i", [])
    n, k = [int(x) for x in input().split()]
    for x in [int(x) for x in input().split()]:
        var.append(x)
    for x in range(k):
        var.insert(0, var.pop(-1))
    print(var[:])


# soal2()

"""Judul Masalah: **Frekuensi Angka Maksimal**

Deskripsi:

Diana, seorang guru matematika, ingin menganalisis hasil ujian matematika siswanya untuk menemukan angka yang paling sering muncul. Informasi ini akan membantu Diana memahami topik mana yang paling banyak siswa kesulitan dengannya. Bantulah Diana menemukan angka dengan frekuensi kemunculan maksimal dalam kumpulan hasil ujian.

Input:

- Baris pertama berisi satu bilangan bulat positif N , jumlah hasil ujian.
- Baris kedua berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili skor dari hasil ujian matematika siswa (0 ≤ skor ≤ 100).

Output:

- Sebuah bilangan bulat yang mewakili angka dengan frekuensi kemunculan maksimal. Jika ada lebih dari satu angka dengan frekuensi maksimal yang sama, cetak angka yang paling kecil.

Contoh Input 1:

5
1 2 3 2 4

Contoh Output 1:

2

Contoh Input 2:

6
4 4 4 3 3 3

Contoh Output 2:

3

Penjelasan:

- Pada Contoh 1, angka 2 muncul dua kali, lebih sering dibandingkan dengan angka lainnya.
- Pada Contoh 2, angka 3 dan 4 muncul tiga kali. Namun, karena kita memilih angka yang paling kecil dari frekuensi maksimal yang sama, jawabannya adalah 3."""


def soal3():
    var = array("i", [])
    svar = array("i", [])
    jvar = array("i", [])
    vvar = array("i", [])
    n = int(input())
    for x in [int(x) for x in input().split()]:
        var.append(x)
    fre = {}

    for element in var:
        if element in fre:
            fre[element] += 1
        else:
            fre[element] = 1

    sor = dict(sorted(fre.items(), key=lambda item: item[1], reverse=True))

    for key in sor:
        # print(f"L1: {key}")
        jvar.append(key)
        vvar.append(sor[key])
        for j in range(sor[key]):
            # print(f'L2: {i}')
            # print(f'sor[key]: {sor[key]}')
            svar.append(key)
    frek = 0
    for i in range(len(vvar) - 1):
        # print(f'Loop: {i}')
        if vvar[i] == vvar[i + 1]:
            if jvar[i] > jvar[i + 1]:
                frek = i + 1
            else:
                pass
        else:
            pass
    # print(svar)
    # print(jvar)
    # print(vvar)
    print(jvar[frek])


"""**Permutasi**

Judul Masalah: **Kemungkinan Permutasi**

Deskripsi:

Eva dan Farhan adalah sahabat yang memiliki dua set angka. Mereka penasaran apakah kedua set tersebut merupakan permutasi satu sama lain, yaitu apakah setiap angka di satu set dapat ditemukan di set lain dengan jumlah yang sama. Bantulah mereka menentukan apakah kedua set angka tersebut adalah permutasi satu sama lain.

Input:

- Baris pertama berisi satu bilangan bulat positif N  jumlah angka dalam setiap set.
- Baris kedua berisi N bilangan bulat yang dipisahkan dengan spasi, mewakili set angka pertama.
- Baris ketiga berisi N bilangan bulat yang dipisahkan dengan spasi, mewakili set angka kedua.

Output:

- Cetak "Ya" jika kedua set angka tersebut adalah permutasi satu sama lain, atau "Tidak" jika bukan.

Contoh Input 1:

3
1 2 3
3 2 1

Contoh Output 1:

Ya

Contoh Input 2:

3
1 1 2
1 2 2

Contoh Output 2:

Tidak

Penjelasan:

- Pada Contoh 1, setiap angka di set pertama dapat ditemukan di set kedua dengan jumlah yang sama. Kedua set adalah permutasi satu sama lain.
- Pada Contoh 2, jumlah angka 1 dan 2 tidak sama di kedua set, sehingga bukan merupakan permutasi satu sama lain.

Zip
"""


def soal4():
    var0 = array("i", [])
    var1 = array("i", [])
    n = int(input())
    for x in [int(x) for x in input().split()]:
        var0.append(x)
    for x in [int(x) for x in input().split()]:
        var1.append(x)
    vars0 = sorted(var0)
    vars1 = sorted(var1)
    for i in range(n):
        if vars0[i] == vars1[i]:
            indikator = "Ya"
        else:
            indikator = "Tidak"
            break
    print(indikator)


"""1. Judul Masalah: **Perbandingan Kinerja Karyawan**

Deskripsi:

Di sebuah perusahaan, terdapat dua tim yang terdiri dari N orang karyawan di masing-masing tim. Setiap bulan, perusahaan melakukan evaluasi kinerja karyawan dengan memberikan skor berdasarkan kontribusi mereka. Manajer ingin melakukan analisis untuk mengetahui seberapa sering karyawan di Tim A memiliki skor yang lebih tinggi dibandingkan karyawan pada posisi yang sama di Tim B, untuk menilai tim mana yang memiliki kinerja lebih baik secara keseluruhan.

Input:

- Baris pertama berisi satu bilangan bulat positif N , jumlah karyawan dalam setiap tim.
- Baris kedua berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili skor kinerja karyawan Tim A.
- Baris ketiga berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili skor kinerja karyawan Tim B.

Output:

- Sebuah bilangan bulat yang mewakili jumlah kali karyawan di Tim A memiliki skor yang lebih tinggi dibandingkan dengan karyawan pada posisi yang sama di Tim B.

Contoh Input 1:

5
3 5 7 5 3
4 5 6 7 1

Contoh Output 1:

2

Contoh Input 2:

3
2 2 2
3 3 3

Contoh Output 2:

0

Penjelasan:

- Pada Contoh 1, karyawan Tim A hanya memiliki skor lebih tinggi pada posisi ketiga dan kelima dibandingkan dengan Tim B, sehingga outputnya adalah 2.
- Pada Contoh 2, tidak ada karyawan di Tim A yang memiliki skor lebih tinggi dari Tim B pada posisi yang sama, sehingga outputnya adalah 0."""


def soal5():
    var0 = array("i", [])
    var1 = array("i", [])
    counter = 0
    n = int(input())
    for x in [int(x) for x in input().split()]:
        var0.append(x)
    for x in [int(x) for x in input().split()]:
        var1.append(x)
    zipped_var = zip(var0, var1)
    for x, y in zipped_var:
        if x > y:
            counter += 1
        else:
            pass
    print(counter)


"""Judul Masalah: **Persediaan Bahan Makanan**

Deskripsi:

Sebuah restoran sedang melakukan inventaris bulanan untuk mengecek persediaan bahan makanannya. Restoran tersebut memiliki dua jenis daftar persediaan: Daftar A menyimpan jumlah bahan makanan yang digunakan selama bulan ini, dan Daftar B menyimpan jumlah bahan makanan yang dibeli selama bulan ini. Manajer ingin mengetahui jumlah total bahan makanan yang tersisa di akhir bulan untuk setiap jenis bahan makanan, dengan asumsi semua bahan makanan dari bulan sebelumnya telah digunakan.

Input:

- Baris pertama berisi satu bilangan bulat positif N , jumlah jenis bahan makanan.
- Baris kedua berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili jumlah penggunaan bahan makanan dari Daftar A.
- Baris ketiga berisi N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili jumlah pembelian bahan makanan dari Daftar B.

Output:

- N bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili jumlah total bahan makanan yang tersisa untuk setiap jenis bahan makanan di akhir bulan.

Contoh Input 1:

4
500 300 400 200
600 400 500 300

Contoh Output 1:

100 100 100 100

Contoh Input 2:

3
250 150 100
300 120 150

Contoh Output 2:

50 -30 50

Penjelasan:

- Pada Contoh 1, untuk setiap jenis bahan makanan, jumlah yang dibeli lebih banyak atau sama dengan jumlah yang digunakan, sehingga semua jenis bahan makanan memiliki sisa 100 unit.
- Pada Contoh 2, jenis bahan makanan kedua digunakan lebih banyak daripada yang dibeli, menghasilkan defisit sebesar 30 unit, sedangkan jenis lainnya memiliki sisa sesuai perhitungan."""


def soal6():
    var0 = array("i", [])
    var1 = array("i", [])
    var2 = array("i", [])
    n = int(input())
    for x in [int(x) for x in input().split()]:
        var0.append(x)
    for x in [int(x) for x in input().split()]:
        var1.append(x)
    zipped_var = zip(var0, var1)
    for x, y in zipped_var:
        var2.append(y - x)
    for element in var2:
        print(element, end=" ")


soal1()
soal2()
soal3()
soal4()
soal5()
soal6()
