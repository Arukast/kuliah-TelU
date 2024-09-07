import numpy as np

# Membuat array NumPy yang merepresentasikan data fasilitas
data = np.array([
    [50, 24, 40, 70],
    [53, 20, 45, 80],
    [70, 50, 60, 90],
    [80, 45, 70, 76],
    [90, 70, 65, 90],
    [88, 86, 80, 80],
    [100, 90, 99, 100]
])

# Nama bulan
bulan = ["Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September"]

# Nama barang
barang = ["AC","Kulkas", "Televisi", "Sofa"]

# Menampilkan data dalam format tabel dengan nama bulan
print("     ====Data Fasilitas Rs. Vitalaya====")
print("\n{:<10} {:<7} {:<9} {:<10} {:<9}".format("Bulan", *barang))
for i in range(len(bulan)):
    print("{:<11}".format(bulan[i]), end="")
    for j in range(len(data[i])):
        print("{:<10}".format(data[i][j]), end="")
    print()

# Masing-masing total Fasilitas untuk setiap produk (Ac, Kulkas, Televisi, Sofa) selama 7 bulan.
total_facilities = np.sum(data, axis=0)

# Menampilkan total fasilitas untuk setiap produk
print("\nTotal Fasilitas untuk setiap produk:")
for i in range(len(barang)):
    print(f"\n{barang[i]}: {total_facilities[i]}")

# Menemukan bulan dengan fasilitas produk terbanyak dan terendah.
max_facility_month_index = np.argmax(np.sum(data, axis=1))
min_facility_month_index = np.argmin(np.sum(data, axis=1))

# Menampilkan bulan dengan fasilitas produk terbanyak dan terendah
print("\nBulan dengan fasilitas produk terbanyak:", bulan[max_facility_month_index])
print("\nBulan dengan fasilitas produk terendah:", bulan[min_facility_month_index])

# Menghitung rata-rata fasilitas kulkas selama 7 bulan terakhir.
avg_fridge_facilities = np.mean(data[:, 1])  # Kulkas adalah kolom kedua (indeks 1)

# Menampilkan rata-rata fasilitas kulkas selama 7 bulan terakhir
print("\nRata-rata fasilitas kulkas selama 7 bulan terakhir:", avg_fridge_facilities)

# Menemukan fasilitas yang sangat kurang dimiliki Rs.vitalaya.
lacking_facility_index = np.argmin(total_facilities)

# Menampilkan fasilitas yang sangat kurang dimiliki Rs. Vitalaya
print("\nFasilitas yang sangat kurang dimiliki Rs. Vitalaya adalah:", barang[lacking_facility_index])
