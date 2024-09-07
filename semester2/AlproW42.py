"""Judul Masalah: Perhitungan Rata-Rata Berat Badan Siswa
Deskripsi:
Seorang guru olahraga di sebuah sekolah ingin mengetahui rata-rata berat badan
siswa di kelasnya untuk mempersiapkan program latihan yang sesuai. Setiap
siswa di kelas memiliki berat badan yang berbeda. Guru tersebut memiliki daftar
berat badan siswa dalam satuan kilogram. Anda diminta untuk membantu guru
tersebut menghitung rata-rata berat badan siswa di kelas.
Input:
Baris pertama berisi sebuah bilangan bulat positif N
N baris berikutnya, setiap baris berisi sebuah bilangan bulat yang mewakili
berat badan setiap siswa dalam kilogram (1 ≤ berat badan ≤ 200).
Output:
Sebuah bilangan desimal yang mewakili rata-rata berat badan siswa di kelas,
dibulatkan hingga dua angka di belakang koma.
Contoh Input 1:
5
50
55
60
45
70
Contoh Output 1:
56.00
Contoh Input 2:
3
40
80
60
Contoh Output 2:
60.00
"""

def soal1():
    data_bb = []
    n = int(input('Jumlah data berat badan yang akan dimasukan: '))
    while n > 0:
        inputan = int(input('Masukan berat badan siswa dalam KG: '))
        if 1 <= inputan <= 200:
            data_bb.append(inputan)
            n -= 1
        else:
            print('Berat badan harus lebih dari sama dengan 1 dan kurang dari sama dengan 200 !')
    print(f'Rata-rata = {((sum(data_bb))/len(data_bb)):.2f}')

"""Judul Masalah: Pencarian Buku di Perpustakaan
Deskripsi:
Sebuah perpustakaan besar memiliki katalog buku yang disimpan dalam format
list yang berisi judul buku. Pengunjung perpustakaan ingin mencari apakah buku
tertentu tersedia di perpustakaan tersebut berdasarkan judul. Anda diminta untuk
membantu pengunjung menemukan buku dengan melakukan pencarian pada list
judul buku. Jika buku ditemukan, program harus mengembalikan pesan bahwa
buku tersebut tersedia. Jika tidak, program harus menyampaikan bahwa buku
tersebut tidak tersedia.
Input:
Baris pertama berisi sebuah bilangan bulat positif N , jumlah buku di
perpustakaan.
N baris berikutnya, setiap baris berisi sebuah string yang mewakili judul buku.
Judul buku hanya terdiri dari huruf dan spasi, dengan panjang maksimal 100
karakter.
Baris terakhir berisi sebuah string yang mencari judul buku yang ingin dicari
oleh pengunjung.
Output:
Sebuah string yang menyatakan "Buku tersedia" jika buku ditemukan dalam
list, atau "Buku tidak tersedia" jika buku tidak ditemukan.
Contoh Input 1:
5
Harry Potter and the Sorcerer's Stone
The Great Gatsby
To Kill a Mockingbird
1984
The Catcher in the Rye
To Kill a Mockingbird
Contoh Output 1:
Buku tersedia
Contoh Input 2:
3
Bumi Manusia
Laskar Pelangi
Dilan 1990
Sapiens: A Brief History of Humankind
Contoh Output 2:
Buku tidak tersedia
"""

def soal2():
    judul_buku = []
    n = int(input('Jumlah judul buku yang akan dimasukan: '))
    while n > 0:
        judul = input('Masukan judul buku: ')
        if len(judul) > 100:
            print('Panjang judul buku maksimal 100 karakter!!!')
        else:
            judul_buku.append(judul)
            n -= 1
    cari = input('Cari: ')
    for buku in judul_buku:
        if cari == buku:
            indikator = 'Buku Tersedia'
            break
        else:
            indikator = 'Buku tidak tersedia'
            pass
    print(indikator)

"""Judul Masalah: Optimalisasi Jadwal Pemutaran Film di Bioskop
Deskripsi:
Sebuah bioskop ingin merencanakan jadwal pemutaran film agar dapat
memaksimalkan jumlah film yang ditayangkan dalam satu hari. Setiap film memiliki
durasi tertentu dan setiap studio hanya tersedia untuk jadwal pemutaran selama
12 jam per hari. Bioskop tersebut ingin mengetahui jumlah maksimal film yang bisa
ditayangkan dalam satu studio tanpa tumpang tindih jadwal.
Input:
Baris pertama berisi dua bilangan bulat positif F dan T , di mana F adalah
jumlah film yang ingin ditayangkan dan T adalah total durasi tersedia dalam
jam untuk satu studio.
F baris berikutnya, setiap baris berisi satu bilangan bulat yang mewakili durasi
setiap film dalam jam (1 ≤ durasi ≤ T).
Output:
Satu bilangan bulat yang mewakili jumlah maksimal film yang bisa ditayangkan
dalam satu studio dalam satu hari.
Contoh Input 1:
5 12
2
3
3
2
1
Contoh Output 1:
5
Contoh Input 2:
4 10
5
5
2
3
Contoh Output 2:
3
Penjelasan:
Pada Contoh 1, terdapat 5 film dengan total durasi tersedia 12 jam. Bioskop
dapat memutar maksimal 5 film dengan memilih film dengan durasi 2, 3, 3, 2,
dan 1 jam.
Pada Contoh 2, dengan total durasi tersedia 10 jam dan 4 film, hanya bisa
memutar maksimal 3 film dengan memilih film dengan durasi 5 , 2 dan 3 jam.
"""

def soal3():
    data_durasi = []
    indikator = 0
    jumlah = 0
    f, t = [int(x) for x in input('Masukan jumlah film dan total durasi tersedia dalam jam untuk satu studio: ').split()]
    while f > 0:
        durasi = int(input('Masukan durasi film dalam jam: '))
        if 1 <= durasi <= t:
            data_durasi.append(durasi)
            f -= 1
        else:
            print(f'durasi harus >= 1 dan <= {t}')
    data_durasi.sort()
    for i in data_durasi:
        indikator += i
        jumlah += 1
        if indikator > t:
            indikator -= i
            jumlah -= 1
            break
        else:
            pass
    print(f'Jumlah maksimal film yang bisa ditayangkan: {jumlah}')

"""Judul Masalah: Analisis Konsumsi Listrik Bulanan
Deskripsi:
Seorang analis data di perusahaan listrik ingin mengevaluasi konsumsi listrik
bulanan pelanggan untuk menentukan strategi tarif baru. Tujuan utamanya adalah
mengidentifikasi pelanggan dengan konsumsi tinggi, sedang, dan rendah
berdasarkan rata-rata konsumsi bulanan mereka. Ada tiga kategori yang
diinginkan: Kategori Tinggi untuk konsumsi ≥ 500 kWh, Kategori Sedang untuk
konsumsi antara 200 kWh dan 499 kWh, dan Kategori Rendah untuk konsumsi <
200 kWh. Analis tersebut memiliki data konsumsi bulanan pelanggan dan ingin
mengetahui jumlah pelanggan di masing-masing kategori.
Input:
Baris pertama berisi satu bilangan bulat positif P jumlah pelanggan.
Baris kedua berisi P bilangan bulat yang dipisahkan dengan spasi, masingmasing mewakili rata-rata konsumsi bulanan pelanggan dalam kWh (0 ≤
konsumsi ≤ 1000).
Output:
Tiga bilangan bulat yang dipisahkan dengan spasi, masing-masing mewakili
jumlah pelanggan di Kategori Tinggi(≥500), Sedang(≥200), dan
Rendah(<200).
Contoh Input 1:
5
520 450 150 600 220
Contoh Output 1:
2 2 1
Contoh Input 2:
3
180 500 299
Contoh Output 2:
1 1 1
Penjelasan:
Pada Contoh 1, terdapat dua pelanggan dengan konsumsi ≥ 500 kWh
(Kategori Tinggi), dua pelanggan dengan konsumsi antara 200 kWh dan 499
kWh (Kategori Sedang), dan satu pelanggan dengan konsumsi < 200 kWh
(Kategori Rendah).
Pada Contoh 2, terdapat satu pelanggan di setiap kategori."""

def soal4():
    data_listrik = []
    tinggi = sedang = rendah = 0
    p = int(input('Masukan jumlah pelanggan: '))
    for x in [int(x) for x in input('Masukan rata-rata konsumsi bulanan setiap pelanggan dalam kWh: ').split()]:
            data_listrik.append(x)
    for kwh in data_listrik:
        if kwh >= 500:
            tinggi += 1
        elif kwh >= 200:
            sedang += 1
        else:
            rendah += 1
    print(f'Tinggi = {tinggi} , Sedang = {sedang} , Rendah = {rendah}')
    
soal1()
soal2()
soal3()
soal4()