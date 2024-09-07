# Import Numpy sebagai npy
import numpy as npy
# Memuat data nama Bahan Makanan dengan bentuk Numpy array dengan nama variabel bahanMakanan
bahanMakanan = npy.array(['Daging Ayam', 'Ikan Salmon', 'Sayuran', 'Bumbu Masak', 'Bawang Merah', 'Tepung', 'Minyak Goreng', 'Gula Pasir', 'Garam', 'Santan'])
# Memuat data Biaya Pembelian dengan bentuk Numpy array dengan nama variabel biayaBeli
biayaBeli = npy.array([100000, 150000, 50000, 30000, 20000, 40000, 60000, 10000, 5000, 25000])
# Memuat data Biaya Tambahan dengan bentuk Numpy array dengan nama variabel biayaTambahan
biayaTambahan = npy.array([20000, 10000, 5000, 15000, 5000, 0, 8000, 3000, 2000, 7000])
# Mengdeklarasikan Numpy array kosong dengan nama variabel totalBiayaBahan
totalBiayaBahan = npy.array([])
# Mengdeklarasikan List kosong dengan nama variabel listBiayaTambahan
listBiayaTambahan = []
# Looping dengan membuat  variabel i dan data dari variabel biayaTambahan yang dimana i sebagai indeks dan data sebagai element indeks ke-i yang diambil dari variabel biayaTambahan dengan menggunakan function enumerate()
for i, data in enumerate(biayaTambahan):
    # Memasukan data kedalaman listBiayaTambahan dengan menggunakan method append()
    listBiayaTambahan.append(data)
    # Memasukan element baru setelah data di dalam totalBiayaBahan ke array totalBiayaBahan dari hasil penjumlahan data ditambah elemen ke-i dari variabel biayaBeli dengan method Numpy append()
    totalBiayaBahan = npy.append(totalBiayaBahan, data + biayaBeli[i])
# Mendeklarasikan dictionary baru dengan nama variabel dataBiaya dari hasil gabungan array bahanMakanan yang sebagai Key dan array totalBiayaBahan yang sebagai Value dengan menggunakan function dict() dan zip()
dataBiaya = dict(zip(bahanMakanan, totalBiayaBahan))
# Mengdeklarasikan variabel baru dengan nama biayaKeseluruhan yang memuat jumlah dari array totalBiayaBahan dengan menggunakan method Numpy sum()
biayaKeseluruhan = npy.sum(totalBiayaBahan)
# Mengdeklarasikan variabel baru dengan nama biayaTambahanTertinggi yang memuat data terbesar dari array biayaTambahan dengan menggunakan method Numpy max()
biayaTambahanTertinggi = npy.max(biayaTambahan)
# Mendeklarasikan variabel baru dengan nama biayaTambahanMakananTertinggi yang memuat data nama bahan makanan dengan biaya tambahan tertinggi dengan cara method index() akan mencari data yang sama dengan data biayaTambahanTertinggi di dalam List listBiayaTambahan, lalu method index() ini akan menghasilkan sebuah indeks, lalu indeks ini akan dipakai untuk memanggil element dari array bahanMakanan, maka element yang dipanggil akan menjadi Value dari variabel biayaTambahanMakananTertinggi
biayaTambahanMakananTertinggi = bahanMakanan[listBiayaTambahan.index(biayaTambahanTertinggi)]
# Mengdeklarasikan variabel baru dengan nama biayaTambahanTerendah yang memuat data terkecil dari array biayaTambahan dengan menggunakan method Numpy min()
biayaTambahanTerendah = npy.min(biayaTambahan)
# Mendeklarasikan variabel baru dengan nama biayaTambahanMakananTerendah yang memuat data nama bahan makanan dengan biaya tambahan terendah dengan cara method index() akan mencari data yang sama dengan data biayaTambahanTerendah di dalam List listBiayaTambahan, lalu method index() ini akan menghasilkan sebuah indeks, lalu indeks ini akan dipakai untuk memanggil element dari array bahanMakanan, maka element yang dipanggil akan menjadi Value dari variabel biayaTambahanMakananTerendah
biayaTambahanMakananTerendah = bahanMakanan[listBiayaTambahan.index(biayaTambahanTerendah)]
# Mendeklarasikan variabel baru dengan nama meanBiayaTambahan yang memuat rata-rata dari array biayaTambahan dengan menggunakan method Numpy mean()
meanBiayaTambahan = npy.mean(biayaTambahan)
# Menampilkan data tiap bahan makanan dalam bentuk dictionary dengan cara memanggil variabel dataBiaya
print(f'\nData biaya tiap bahan makanan: {dataBiaya}\n')
# Menampilkan biaya keseluruhan dari pembelian bahan makanan dengan cara memanggil variabel biayaKeseluruhan
print(f'Total biaya keseluruhan untuk pembelian bahan makanan: Rp{biayaKeseluruhan}\n')
# Menampilkan bahan makanan dengan biaya tambahan tertinggi beserta biaya tambahannya dengan cara memanggil variabel biayaTambahanMakananTertinggi dan variabel biayaTambahanTertinggi
print(f'Bahan makanan dengan biaya tambahan tertinggi: {biayaTambahanMakananTertinggi} dengan biaya tambahan sebesar Rp{biayaTambahanTertinggi}\n')
# Menampilkan bahan makanan dengan biaya tambahan terendah beserta biaya tambahannya dengan cara memanggil variabel biayaTambahanMakananTerendah dan variabel biayaTambahanTerendah
print(f'Bahan makanan dengan biaya tambahan terendah: {biayaTambahanMakananTerendah} dengan biaya tambahan sebesar Rp{biayaTambahanTerendah}\n')
# Menampilkan rata-rata biaya tambahan bahan makanan dengan cara memanggil variabel meanBiayaTambahan
print(f'Rata-rata biaya tambahan bahan makanan: Rp{meanBiayaTambahan}\n')