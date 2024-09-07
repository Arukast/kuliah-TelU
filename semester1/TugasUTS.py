# NIM: 102022300301
# Nama: Tb. Alta Ulil Abshor

print("=== Tugas 1 - Program Pembelian ===")
# Fumgsi Pembayaran


def pembayaran_0301(tota_0301):
    #  Pengecekan untuk mendapat diskon
    print("--- Proses Pembayaran ---")
    if tota_0301 > 500000:
        diskon_0301 = 0.75
        print(
            "Selamat Anda mendapat diskon 25% karena total harga Anda lebih besar dari Rp. 500000")
        total_akhir_0301 = tota_0301 * diskon_0301
        print(f"Total harga setelah diskon adalah: Rp. {total_akhir_0301}")
    elif tota_0301 > 250000:
        diskon_0301 = 0.85
        print(
            "Selamat Anda mendapat diskon 15% karena total harga Anda lebih besar dari Rp. 250000")
        total_akhir_0301 = tota_0301 * diskon_0301
        print(f"Total harga setelah diskon adalah: Rp. {total_akhir_0301}")
    elif tota_0301 > 100000:
        diskon_0301 = 0.9
        print(
            "Selamat Anda mendapat diskon 10% karena total harga Anda lebih besar dari Rp. 100000")
        total_akhir_0301 = tota_0301 * diskon_0301
        print(f"Total harga setelah diskon adalah: Rp. {total_akhir_0301}")
    else:
        diskon_0301 = 1
        total_akhir_0301 = tota_0301 * diskon_0301
    print(f"Tagihan Anda: Rp. {total_akhir_0301}")
    nim_0301 = int(input("Masukan NIM Anda: "))
    nama_0301 = input("Masukan nama Anda: ")
    nominal_pembayaran_0301 = float(
        input("Masukan nominal pembayaran Anda: Rp. "))
    # pengecekan nominal dan kembalian
    if nominal_pembayaran_0301 >= total_akhir_0301:
        kembalian_0301 = nominal_pembayaran_0301 - total_akhir_0301
        print(f"Kembalian Anda adalah: Rp. {kembalian_0301}")
        print(
            f"--- Transaksi dengan NIM {nim_0301} dan nama {nama_0301} , telah selesai ---")
    else:
        print(f"Pembayaran gagal karena nominal pembayaran Anda kurang!")

# Fungsi menu minuman


def menu_minuman_0301():
    list_0301 = {
        "Jus Buah": 15000,
        "Kopi": 20000,
        "Teh": 7000,
        "Air Mineral": 25000,
        "Coke": 10000
    }
    # Nampilin menu
    print("--- Menu Minuman ---")
    for x_0301 in list_0301:
        print(f"{x_0301} : Rp. {list_0301.get(x_0301)}")
    # Input pesanan
    print("--- Pemesanan ---")
    berapa_0301 = int(input("Berapa macam minuman yang akan Anda pilih: "))
    pesanan_minuman_0301 = []
    jumlah_minuman_0301 = []
    total_perminuman_0301 = []
    if berapa_0301 < 6:
        while berapa_0301 > 0:
            terpilih_0301 = input("Pilih Minuman Anda: ")
            if terpilih_0301.title() in list_0301 and terpilih_0301.title() not in pesanan_minuman_0301:
                jumlah_terpilih_0301 = int(
                    input(f"Berapa jumlah {terpilih_0301.title()} yang Anda mau: "))
                pesanan_minuman_0301.append(terpilih_0301.title())
                jumlah_minuman_0301.append(jumlah_terpilih_0301)
                total_perminuman_0301.append(
                    jumlah_terpilih_0301 * list_0301.get(terpilih_0301.title()))
                print(f"Pesanan {terpilih_0301.title()} tercatat")
                berapa_0301 -= 1
            elif terpilih_0301.title() in list_0301 and terpilih_0301.title() in pesanan_minuman_0301:
                print(f"{terpilih_0301.title()} sudah tercatat di pesanan Anda")
            else:
                print("Minuman tidak ada di menu")
    else:
        print("Maksimal hanya 5 macam Minuman!")
        return
    # Menampilkan Pesanan
    print("--- Pesanan Anda ---")
    for (x_0301, y_0301, z_0301) in zip(pesanan_minuman_0301, jumlah_minuman_0301, total_perminuman_0301):
        print(
            f"{y_0301} {x_0301} dengan harga satuan Rp. {list_0301.get(x_0301)} , jadi total harga {y_0301} {x_0301} adalah Rp. {z_0301}")
    # menghitung dan menampilkan total harga keseluruhan
    print("--- Total harga keseluruhan ---")
    total_harga_0301 = float(sum(total_perminuman_0301))
    print(f"Total harga yang harus Anda bayar adalah: Rp. {total_harga_0301}")
    # Menuju ke fungsi pembayaran
    pembayaran_0301(total_harga_0301)

# Fungsi menu makanan


def menu_makanan_0301():
    list_0301 = {
        "Nasgor": 10000,
        "Omelet": 15000,
        "Indomie": 5000,
        "Sushi": 100000,
        "Ramen": 75000
    }
    # Nampilin menu
    print("--- Menu Makanan ---")
    for x_0301 in list_0301:
        print(f"{x_0301} : Rp. {list_0301.get(x_0301)}")
    # Input pesanan
    print("--- Pemesanan ---")
    berapa_0301 = int(input("Berapa macam makanan yang akan Anda pilih: "))
    pesanan_makanan_0301 = []
    jumlah_makanan_0301 = []
    total_permakanan_0301 = []
    if berapa_0301 < 6:
        while berapa_0301 > 0:
            terpilih_0301 = input("Pilih Makanan Anda: ")
            if terpilih_0301.title() in list_0301 and terpilih_0301.title() not in pesanan_makanan_0301:
                jumlah_terpilih_0301 = int(
                    input(f"Berapa jumlah {terpilih_0301.title()} yang Anda mau: "))
                pesanan_makanan_0301.append(terpilih_0301.title())
                jumlah_makanan_0301.append(jumlah_terpilih_0301)
                total_permakanan_0301.append(
                    jumlah_terpilih_0301 * list_0301.get(terpilih_0301.title()))
                print(f"Pesanan {terpilih_0301.title()} tercatat")
                berapa_0301 -= 1
            elif terpilih_0301.title() in list_0301 and terpilih_0301.title() in pesanan_makanan_0301:
                print(f"{terpilih_0301.title()} sudah tercatat di pesanan Anda")
            else:
                print("Makanan tidak ada di menu")
    else:
        print("Maksimal hanya 5 macam makanan!")
        return
    # Menampilkan Pesanan
    print("--- Pesanan Anda ---")
    for (x_0301, y_0301, z_0301) in zip(pesanan_makanan_0301, jumlah_makanan_0301, total_permakanan_0301):
        print(
            f"{y_0301} {x_0301} dengan harga satuan Rp. {list_0301.get(x_0301)} , jadi total harga {y_0301} {x_0301} adalah Rp. {z_0301}")
    # menghitung dan menampilkan total harga keseluruhan
    print("--- Total harga keseluruhan ---")
    total_harga_0301 = float(sum(total_permakanan_0301))
    print(f"Total harga yang harus Anda bayar adalah: Rp. {total_harga_0301}")
    # Menuju ke fungsi pembayaran
    pembayaran_0301(total_harga_0301)


# menu utama
print("--- Menu Utama ---")
print("Selamat datang")
print("Disini terdapat dua menu, yaitu makanan dan minuman. Anda hanya bisa memilih salah satu menu saja")
pemanggil_0301 = input("Silahkan pilih salah satu menu: ")
if pemanggil_0301.capitalize() == "Makanan":
    menu_makanan_0301()
elif pemanggil_0301.capitalize() == "Minuman":
    menu_minuman_0301()
else:
    print("menu yang Anda sebutkan tidak ada!")

print("=== Tugas 2 - Program ATM ===")

database_alta_0301 = {
    'NIM': '102022300301',
    'Nama': 'Tb. Alta Ulil Abshor',
    'No. Rekening': 1234567890,
    'PIN': 300301,
    'Saldo': 1000000
}
database_admin_0301 = {
    'NIM': '102022300300',
    'Nama': 'Admin',
    'No. Rekening': 1,
    'PIN': 123456,
    'Saldo': 1000000
}
nim_0301 = [database_alta_0301.get(
    'NIM'), database_admin_0301.get('NIM'),]
nama_0301 = [database_alta_0301.get(
    'Nama'), database_admin_0301.get('Nama'),]
norek_0301 = [database_alta_0301.get(
    'No. Rekening'), database_admin_0301.get('No. Rekening')]
pin_0301 = [database_alta_0301.get(
    'PIN'), database_admin_0301.get('PIN')]
saldo_0301 = [database_alta_0301.get(
    'Saldo'), database_admin_0301.get('Saldo')]


def menu_cek_saldo_0301(user_0301):
    print('--- Menu Cek Saldo ---')
    print(
        f'Informasi Anda:\nNIM: {user_0301}\nNama: {nama_0301[nim_0301.index(user_0301)]}\nNomor Rekening: {norek_0301[nim_0301.index(user_0301)]}')
    print(f'- Saldo Anda: \n-> Rp. {saldo_0301[nim_0301.index(user_0301)]}')


def menu_tarik_uang_0301(user_0301):
    print('--- Menu Tarik Uang ---')
    print(
        f'Informasi Anda:\nNIM: {user_0301}\nNama: {nama_0301[nim_0301.index(user_0301)]}\nNomor Rekening: {norek_0301[nim_0301.index(user_0301)]}')
    print(f'- Saldo Anda: \n-> Rp. {saldo_0301[nim_0301.index(user_0301)]}')
    tarik_menu_0301 = int(input('Masukan nominal yang ingin Anda tarik: Rp. '))
    sakhir_menu_0301 = saldo_0301[nim_0301.index(user_0301)] - tarik_menu_0301
    database_alta_0301.update({'Saldo': sakhir_menu_0301})
    print(f'- Saldo akhir Anda: \n-> Rp. {sakhir_menu_0301}')


def menu_setor_uang_0301(user_0301):
    print('--- Menu Setor Uang ---')
    print(
        f'Informasi Anda:\nNIM: {user_0301}\nNama: {nama_0301[nim_0301.index(user_0301)]}\nNomor Rekening: {norek_0301[nim_0301.index(user_0301)]}')
    print(f'- Saldo Anda: \n-> Rp. {saldo_0301[nim_0301.index(user_0301)]}')
    tarik_menu_0301 = int(input('Masukan nominal yang ingin Anda setor: Rp. '))
    sakhir_menu_0301 = saldo_0301[nim_0301.index(user_0301)] + tarik_menu_0301
    database_alta_0301.update({'Saldo': sakhir_menu_0301})
    print(f'- Saldo akhir Anda: \n-> Rp. {sakhir_menu_0301}')


def menu_utama_0301(user_0301):
    print('--- Selamat Datang di menu Utama! --- \nSilahkan pilih menu selanjutnya')
    print('-> Cek Saldo\n-> Tarik Uang\n-> Setor Uang')
    utama_next_0301 = input('Anda ingin menuju ke menu: ')
    if utama_next_0301.title() == 'Cek Saldo':
        menu_cek_saldo_0301(user_0301)
    elif utama_next_0301.title() == 'Tarik Uang':
        menu_tarik_uang_0301(user_0301)
    elif utama_next_0301.title() == 'Setor Uang':
        menu_setor_uang_0301(user_0301)
    else:
        print('Menu yang Anda ingin tuju tidak ada!')


def login_0301():
    print('--- Selamat Datang di menu login! --- \nSilahkan masukan informasi Anda!')
    login_nim_0301 = input("Masukan NIM Anda: ")
    login_nama_0301 = input("Masukan Nama Anda: ")
    login_norek_0301 = int(input("Masukan nomor rekening Anda: "))
    norek_pin_0301 = int(input("Masukan PIN Anda: "))
    if login_nim_0301 in nim_0301 and login_nama_0301 == nama_0301[nim_0301.index(login_nim_0301)] and login_norek_0301 == norek_0301[nim_0301.index(login_nim_0301)] and norek_pin_0301 == pin_0301[nim_0301.index(login_nim_0301)]:
        print("Login successful! \nMenuju ke menu utama")
        menu_utama_0301(login_nim_0301)
    else:
        print("Informasi yang Anda masukan tidak sesuai!")


login_0301()
