"""Pak Budi adalah pemilik dari sebuah kos-kosan yang bernama "Budi Kost". Ia ingin
membuat sistem untuk memantau pembayaran bulanan dari penghuni kos. Koskosan ini memiliki 8 kamar dengan tarif berbeda dan beberapa penghuni memiliki
tunggakan dari bulan sebelumnya. Pak Budi ingin menggunakan Python dan
NumPy untuk mempermudah penghitungan total pemasukan bulanan, tunggakan,
dan juga ingin mengetahui kamar mana yang paling sering memiliki tunggakan.
Berikut adalah data tarif bulanan dan tunggakan (jika ada) untuk tiap kamar:
No. Kamar Tarif Bulanan (Rp) Tunggakan (Rp)
1 1.500.000 0
2 1.500.000 300.000
3 1.500.000 150.000
4 2.000.000 0
5 1.800.000 0
6 1.800.000 500.000
7 2.000.000 250.000
8 2.000.000 0
Program tersebut harus mampu:
Menampilkan data tagihan tiap kamar termasuk tunggakan dan diskon dalam
bentuk dictionary.
Menghitung total pemasukan bulanan termasuk pembayaran tunggakan dan
diskon.
Mengidentifikasi kamar dengan tunggakan tertinggi.
Menghitung rata-rata tarif bulanan (tidak termasuk diskon dan tunggakan).
Menyediakan informasi tentang jumlah total tunggakan yang ada.
Menyediakan informasi tentang jumlah total diskon yang ada.
Diskon diberikan 5% kepada pemilik yang tidak ada tunggakan
Bantu Pak Budi Untuk membuat Program Python"""
import numpy as npy
# Mendefinisikan setiap nomor kamar
noKamar = npy.array(range(1, 9))
# Mendefinisikan tarif bulanan tiap kamar
tarifBulanan = npy.array([1500000, 1500000, 1500000, 2000000, 1800000, 1800000, 2000000, 2000000])
# Mendefinisikan tunggakan tiap kamar
tunggakan = npy.array([0, 300000, 150000, 0, 0, 500000, 250000, 0])
# Mendefinisikan array baru untuk memuat total tagihan yang akan dihitung
totalTagihan = npy.array([])
# Mendefinisikan array baru untuk memuat total diskon yang akan dihitung
totalDiskon = npy.array([])
# Mendefinisikan list baru untuk memuat data tunggakan yang akan dimasukan
listTunggakan = []
# Perulangan yang menghasilkan variabel indeks array tunggakan dan element array tunggakan
for i, data in enumerate(tunggakan):
    # Memasukan element tunggakan yang diiterasi kedalam list
    listTunggakan.append(data)
    # Percabangan untuk mengecek apakah element iterasi tunggakan sama dengan 0
    if data == 0:
        # Menghitung element ke-i dari tarifBulanan dikali dengan 0.95 lalu dimasukan ke array totalTagihan
        totalTagihan = npy.append(totalTagihan, tarifBulanan[i] * 0.95)
        # Menghitung element ke-i dari tarifBulanan dikali dengan 0.05 lalu dimasukan ke array totalDiskon
        totalDiskon = npy.append(totalDiskon, tarifBulanan[i] * 0.05)
    else:
        # Menghitung element ke-i dari tarifBulanan ditambah dengan variabel data lalu dimasukan ke array totalTagihan
        totalTagihan = npy.append(totalTagihan, tarifBulanan[i] + data)
# Menggabungkan array noKamar dan array totalTagihan menjadi dictionary dataTagihan yang dimana array noKamar menjadi key dan array totalTagihan menjadi value
dataTagihan = dict(zip(noKamar, totalTagihan))
# Menampilkan dictionary tagihan
print(f'Data tagihan tiap kamar: {dataTagihan}')
# Menampilkan jumlah dari array totalTagihan menggunakan metode sum
print(f'Total pemasukan bulanan: Rp{npy.sum(totalTagihan)}')
# Menampilkan nomor kamar dengan tunggakan tertinggi berdasarkan: indeks dari nilai tertinggi pada array tunggakan lalu indeksnya ditambah 1
print(f'Kamar dengan tunggakan tertinggi: {listTunggakan.index(npy.max(tunggakan))+1}')
# Menampilkan rata-rata tarif bulanan menggunakan metode mean berdasarkan array tarifBulanan
print(f'Rata-rata tarif bulanan: Rp{npy.mean(tarifBulanan)}')
# Menampilkan jumlah tunggakan menggunakan metode sum berdasarkan array tunggakan
print(f'Jumlah total tunggakan yang ada: Rp{npy.sum(tunggakan)}')
# Menampilkan jumlah diskon menggunakan metode sum berdasarkan array totalDiskon
print(f'Jumlah total diskon: Rp{npy.sum(totalDiskon)}')