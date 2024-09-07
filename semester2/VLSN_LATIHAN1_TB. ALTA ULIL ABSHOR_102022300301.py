def totalPembelian(jumlahHarga):
    if jumlahHarga > 300000:
        diskon = 0.1
        print('Diskon 10% diberikan')
        jumlahHarga -= jumlahHarga*diskon
    elif jumlahHarga >= 100000:
        diskon = 0.05
        print('Diskon 5% diberikan')
        jumlahHarga -= jumlahHarga*diskon
    return jumlahHarga

def cek():
    while True:
        match input('Apakah ada barang lain yang ingin dibeli lagi (y/n): ').lower():
            case 'y':
                return 'y'
            case 'n':
                return 'n'
            case _:
                print('Pilihan tidak valid!')

def main():
    jumlahHarga = 0
    while True:
        print('--- Toko Sembako Amel ---\n1. Beli Beras (Rp16.000/KG)\n2. Beli Telur (Rp32.000/KG)\n3. Beli Gula (Rp12.000/KG)\n4. Selesai Belanja')
        match input('Pilih nomor barang yang ingin dibeli: '):
            case '1':
                jumlahHarga += 16000 * (int(input('Masukan jumlah Beras yang ingin dibeli (KG): ')))
            case '2':
                jumlahHarga += 32000 * (int(input('Masukan jumlah Telur yang ingin dibeli (KG): ')))
            case '3':
                jumlahHarga += 12000 * (int(input('Masukan jumlah Gula yang ingin dibeli (KG): ')))
            case '4':
                return jumlahHarga
            case _:
                print('Pilihan tidak valid!')
        



total = main()
print('Total harga pembelian sebelum diskon', total)
totaldiskon = totalPembelian(total)
print('Total harga setelah diskon: ', totaldiskon)