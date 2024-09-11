print('=== Sistem Manajemen Toko ===')

# Fungsi penjualan ini adalah untuk melakukan penginputan barang dan jumlah barang yang ingin dijual oleh pengguna dan penghitung total harga
def penjualan(inventaris):
    print('--- Transaksi Penjualan ---')
    while True:
        print('\nInventaris Produk:')
        for i, produk in enumerate(inventaris, start=1):
            print(f'{i}. {produk['nama']} - Harga: {produk['harga']} - Stok: {produk['stok']}')
        pilihan_produk = int(input('\nPilih produk yang ingin dijual (1-5): ')) - 1
        if 0 <= pilihan_produk < len(inventaris):
            produk = inventaris[pilihan_produk]
            if produk['stok'] == 0:
                print(f'Stok {produk['nama']} habis!')
            else:
                jumlah_produk = int(input(f'Masukan jumlah {produk['nama']} yang ingin dijual: '))
                if jumlah_produk > produk['stok']:
                    print(f'Stok {produk['nama']} hanya tersedia sejumlah {produk['stok']} stok!\nTolong masukan jumlah yang tidak melebihi dari stok yang ada!')
                elif jumlah_produk <= 0:
                    print('Tolong masukan jumlah yang benar!')
                else:
                    total = produk['harga'] * jumlah_produk
                    return produk, jumlah_produk, total
        else:
            print('Tolong masukan nomor produk yang benar!')

# Fungis diskon_hitung ini adalah untuk menentukan diskon yang didapat dan memperhitungkan total akhir setelah diskon
def diskon_hitung(total):
    if total > 1000000:
        diskon = 0.85
        penyebutan_diskon = '15%'
    elif total > 500000:
        diskon = 0.9
        penyebutan_diskon = '10'
    else:
        diskon = 1
        penyebutan_diskon = 'Tidak ada'
    total_akhir = total * diskon
    return penyebutan_diskon, total_akhir

# Tujuan fungsi struk_pembelian ini adalah untuk menampilkan produk yang dibeli beserta jumlah, harga, total harga, total penjualan dan diskon
def struk_pembelian(produk, jumlah_produk, diskon, total_akhir, total):
    print('\n')
    print('--- Struk Pembelian ---')
    print(f'{produk['nama']} (x{jumlah_produk}) - Harga: {produk['harga']}, Total: {total}\nTotal penjualan: {total_akhir}\nDiskon: {diskon}')

# Tujuan fungsi main_menu ini adalah sebagai pengatur alur jalannya program dan penyimpan data yang ada
def main_menu():
# 3. Buat sebuah list yang berperan sebagai penyimpan data inventaris produk
    inventaris = [
    {'nama' : 'Processor', 'harga' : 200000, 'stok' : 13},
    {'nama' : 'Motherboard', 'harga' : 150000, 'stok' : 17},
    {'nama' : 'RAM', 'harga' : 50000, 'stok' : 35},
    {'nama' : 'Power Supply', 'harga' : 80000, 'stok' : 5},
    {'nama' : 'Graphic Card', 'harga' : 250000, 'stok' : 7}
    ]
# 4. Buat sebuah variabel untuk menghitung total penjualan
    total_penjualan = 0
# 5. Buat fungsi pengulangan untuk terus menjalankan program sampai pengguna meminta untuk berhenti
    while True:
# 6. Disini dilakukan pemanggilan fungsi penjualan untuk memilihi produk dan memasukan jumlah yang dipilih
        produk, jumlah_produk, total = penjualan(inventaris)
# 7. Pengurangan stok dari produk terpilih
        produk['stok'] -= jumlah_produk
# 8. Menghitung total penjualan
        total_penjualan += total
# 9. Pemanggilan fungsi diskon_hitung untuk menghitung diskon
        diskon, total_akhir = diskon_hitung(total_penjualan)
# 10. Pemanggilan fugnsi struk_pembelian untuk menampilkan produk yang dibeli beserta jumlah, harga, total harga, total penjualan dan diskon
        struk_pembelian(produk, jumlah_produk, diskon, total_akhir, total)
        print('\n')
# 11. Perulangan untuk melanjutkan atau memberhentikan program
        pilihan = input('Apakah Anda ingin melanjutkan transaksi (y/n): ').casefold()
        if pilihan == 'y':
            pass
        elif pilihan == 'n':
            print('Terima kasih, program Berakhir')
            break
        else:
            print('Error!')
            break
# 2. panggil fungsi utama yang berperan sebagai pengatur alur program           
main_menu()
