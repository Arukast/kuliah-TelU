try:
    import datetime

    print('=== Program Parkir Dimulai ===')
    # Fungsi ini adalah untuk memasukan input pilihan menu dari pengguna. Fungsi ini dimulai dengan program meminta pengguna memasukan angka pilihan menu, lalu me-return nilai yang tadi dimasukan pengguna. Di dalam fungsi ini terdapat exception ValueError, yang dimana akan berjalan ketika pengguna memasukan huruf, lalu program akan men-display ucapan 'Tolong masukan nomor menu!' dan me-return None.
    def pilihan_menu():
        try:
            x = int(input('Masukan pilihan menu: '))
            return x
        except ValueError:
            print('Tolong masukan nomor menu!')
            return None

    # Fungsi ini adalah untuk mencari index suatu data pada list. Fungsi ini dimulai dengan menerima parameter 'data' dan 'plat', lalu program akan masuk ke perulangan dan mengecek apakah ada data di dalam list 'data' yang sama dengan variable 'plat'. Jika sama, maka akan me-return indeks dari data yang sama. jika tidak, maka akan terus melakukan perulangan. Jadi jika plat yang dicari sama dengan plat yang ada list maka fungsi ini akan me-return index dari data tersebut, jika tidak sama maka akan lanjut dan mengecek data dari list yang lain. 'enumerate()' digunakan untuk mengembalikan indeks dan nilai dari setiap elemen dalam objek yang dapat diiterasi atau diulang-ulang seperti list, tupel, atau string. Jadi dalam setiap iterasi atau perulangan, enumerate() mengembalikan sepasang (indeks, nilai), di mana indeks adalah indeks dari elemen saat ini dalam objek yang diberikan, dan nilai adalah nilai dari elemen tersebut.
    def pencari(data, plat):
        for i, x in enumerate(data):
            if x['plat'] == plat:
                return i
            else:
                pass

    # Fungsi ini digunakan untuk melakukan pembayaran ketika akan keluar area parkir. Fungsi ini dimulai dengan menerima parameter data yang berbentuk tuple (karena banyak argumen yang diterima), lalu men-display durasi lalu akan masuk percabangan untuk mengecek apakah pengguna terkena denda atau tidak. Jika tidak maka hanya men-display total biaya parkir, jika terkena denda maka akan men-display total biaya parkir sebelum terkena denda, lalu memberikan penjelasan kenapa terkena denda dan akan menampilkan berapa denda yang diterima, setelah itu akan men-display berapa total biaya parkir setelah denda. Jika sudah program akan masuk ke perulangan, dan di perulangan pengguna diminta untuk memasukan nominal, dan juga di perulangan terdapat exception jika pengguna memasukan huruf. Setelah itu program akan menghitung kembalian dan men-displaynya, lalu me-return kembalian dan nominal.
    def pembayaran(*data):
        print(f'Durasi Anda selama parkir: {data[2]} detik')
        if data[3] == 0 and data[4] == 0 and data[5] == 0 and data[6] == 0:
            print(f'Total biaya parkir: Rp{data[1]}')
        else:
            print(f'Total biaya parkir: Rp{data[0]}')
            print(f'Dikarenakan Anda melebihi batas waktu maksimal parkir dan Anda lebih dari {data[5]} menit atau {data[6]} detik, maka Anda mendapatkan denda sebesar {data[3]} dari total biaya parkir, yaitu: Rp{data[4]}')
            print(f'Total biaya parkir setelah denda: Rp{data[1]}')
        while True:
            try:
                nominal = int(input('Masukan nominal pembayaran Anda atau ketik "0" untuk pembayaran non-cash: '))
                if nominal >= data[1]:
                    break
                elif nominal == 0:
                    nominal = data[1]
                    break
                else:
                    print('Nominal pembayaran Anda kurang!')
            except ValueError:
                print('Tolong masukan angka! (Jangan huruf)') 
        kembalian = int(nominal - data[1]) 
        print(f'Kembalian Anda: Rp{kembalian}')
        return kembalian, nominal

    # Fungsi ini digunakan untuk menghitung durasi parkir pengguna. Fungsi ini dimulai dari menerima parameter list data dan indeks, lalu mendefinisikan beberapa variabel default, lalu menghitung total durasi parkir pengguna. Setelah itu program akan masuk ke percabangan untuk mendefinisikan biaya parkir sesuai durasi, lalu  program akan menghitung total tagihan, setelah itu program akan me-return setiap variabel yang ada di fungsi ini.
    def hitung_parkir(data, indeks):
        detik = 0
        menit = 0
        denda = 0
        denda_str = 0
        total_durasi = float('{:.2f}'.format((data[indeks]['durasi_akhir'] - data[indeks]['durasi_awal']).total_seconds()))
        if total_durasi <= 60:
            tagihan_awal = 10000
        elif total_durasi <= 120:
            tagihan_awal = 20000
        elif total_durasi <= 180:
            tagihan_awal = 30000
        elif total_durasi <= 240:
            tagihan_awal = 40000
        elif total_durasi <= 360:
            detik = 240
            menit = 4
            denda_str = '10%'
            tagihan_awal = 40000
            denda = int(tagihan_awal * 0.1)
        else:
            detik = 360
            menit = 6
            denda_str = '25%'
            tagihan_awal = 40000
            denda = int(tagihan_awal * 0.25)
        
        tagihan_akhir = int(tagihan_awal + denda)
        return tagihan_awal, tagihan_akhir, total_durasi, denda_str, denda, menit, detik

    # Fungsi ini diguanakan untuk memasukan data kendaraan pengguna ketika akan masuk area parkir. Fungsi ini dimulai dengan menerima parameter list data, lalu men-display ucapan selamat datang, lalu pengguna diminta memasukan plat kendaraan. Setelah itu program akan masuk ke percabangan untuk mengecek apakah plat yang dimasukan pengguna sudah ada di area parkir atau belum. Jika belum, program akan memasukan data plat, waktu masuk, dan durasi awal ke dalam list nested dictionary data, lalu program akan men-display ucapan silahkan masuk, lalu program akan me-return list data. Jika plat pengguna sudah ada di area parkir, maka program akan men-display ucapan 'Plat Anda sudah terdata di area parkir!'.
    def masuk_kendaraan(data):
        print('--- Selamat Datang di menu Masuk Area Parkir ---')
        masukan_plat = input('Masukan plat nomor kendaraan Anda: ') 
        indeks = pencari(data, masukan_plat)
        if indeks == None:
            data.append({
                'plat' : masukan_plat,
                'waktu_masuk' : datetime.datetime.now().strftime('%M:%S'),
                'durasi_awal' : datetime.datetime.now()
            })
            print('Gerbang Terbuka, Silahkan Masuk')
        else:
            print('Plat Anda sudah terdata di area parkir!')
        return data

    # Fungsi ini digunakan pengguna ketika akan keluar dari area parkir. Fungsi ini dumulai dengan menerima parameter list data dan list riwayat, lalu program akan men-display ucapan selamat datang. Setelah itu pengguna akan diminta memasukan plat kendaraan, lalu program akan masuk ke fungsi pencari dengan memberikan argument 'data' dan 'plat' untuk mencari indeks plat yang telah dimasukan pengguna. Setelah itu program mendifinisikan data yang sesuai indeks tadi sebagai variable 'data_pilihan', lalu program akan memasukan data 'waktu_akhir' dan 'durasi_akhir' ke variable 'data_pilihan'. Setelah itu program akan memanggil fungsi 'hitung_parkir' dengan memberikan argumen 'data' dan 'plat_indeks', lalu fungsi 'hitung_parkir' akan me-return variabel 'tagihan_awal', 'tagihan_akhir', 'durasi', 'denda', 'total_denda', 'menit', dan 'detik'. Setelah itu program akan memanggil fungsi 'pembayaran' dengan memberikan varibable argumen yang telah di-return tadi oleh fungsi 'hitung_parkir', lalu fungsi 'pembayaran' akan me-return variable 'kembalian', dan 'nominal'. Setelah itu program akan men-display ucapan 'Selamat Jalan dan Terima Kasih', lalu program akan membuat data 'tagihan', durasi, 'nominal' dan 'kembalian' ke variable 'data_pilihan'. Setelah itu program akan menambahkan data dari variable 'data_pilihan' ke variable list 'riwayat', lalu menghapus data yang sesuai dengan indeks dari plat yang dimasukan pengguna sebelumnya dari list 'data', lalu program akan me-return list 'data' dan list 'riwayat'. Di fungsi ini juga terdapat exception TypeError, exception berjalan ketika pengguna belum masuk area parkir tapi minta untuk keluar area parkir dan program akan me-display ucapan 'Plat kendaraan Anda tidak ada, Anda harus masuk ke parkiran terlebih dahulu!'.
    def keluar_kendaraan(data, riwayat):
        try:
            print('--- Selamat Datang di menu Keluar Area Parkir ---')
            plat = input('Masukan nomor plat kendaraan Anda: ')
            plat_indeks = pencari(data, plat)
            data_pilihan = data[plat_indeks]
            data_pilihan.update({
                'waktu_akhir' : datetime.datetime.now().strftime('%M:%S'),
                'durasi_akhir' : datetime.datetime.now()
            })
            tagihan_awal, tagihan_akhir, durasi, denda, total_denda, menit, detik = hitung_parkir(data, plat_indeks)
            kembalian, nominal = pembayaran(tagihan_awal, tagihan_akhir, durasi, denda, total_denda, menit, detik)
            print('Selamat Jalan dan Terima Kasih')
            data_pilihan.update({
                'tagihan' : int(tagihan_akhir),
                'durasi' : durasi,
                'nominal' : int(nominal),
                'kembalian' : int(kembalian)
            })
            riwayat.append(data_pilihan)
            data.pop(plat_indeks) 
        except TypeError:
            print('Kendaraan Anda tidak terdata di dalam area parkir, Anda harus masuk ke parkiran terlebih dahulu!')
        return data, riwayat

    # Fungsi ini digunakan sebagai menu admin. Fungsi ini dimulai dengan menerima parameter  'riwayat' dan 'pin'. Setelah itu pengguna diminta untuk memasukan PIN admin, lalu program akan masuk ke percabangan untuk mengecek apakah PIN yang dimasukan pengguna sesuai dengan PIN yang ada di data. Jika PIN yang dimasukan pengguna salah, maka program akan men-display 'PIN Admin yang Anda masukan salah!' lalu akan kembali ke menu utama. Jika PIN yang dimasukan pengguna benar, maka program akan masuk ke perulangan. Di dalam perulangan program akan menampilkan ucapan selamat datang dan tiga menu yang ada di fungsi ini. Setelah itu program akan masuk ke fungsi 'pilihan_menu' lalu pengguna diminta untuk memasukan salah satu nomor pilihan menu, jika memilih menu 1, maka program akan menampilkan riwayat transaksi parkir, jika memilih menu 2, maka program akan kembali ke menu utama, jika memilih menu 3, maka program parkir akan berhenti. Di fungsi ini juga terdapat exception ValuError, exception ini akan berjalan ketika pengguna memasukan huruf ketika diminta memasukan PIN. jika exception ini berjalan, maka program akan men-display 'Tolong masukan angka PIN yang benar!' dan kembali ke menu utama.
    def admin_parkir(riwayat, pin):
        try:
            kunci = int(input('Masukan PIN Admin: '))
            if kunci == pin:
                while True:
                    print('--- Selamat Datang di Menu Admin ---\nPilihan Menu:\n1. Cetak seluruh transaksi parkir\n2. Kembali ke Menu Utama\n3. Keluar Program')
                    pilihan = pilihan_menu()
                    if pilihan == 1:
                        print('Riwayat Transaksi Parkir:')
                        for i, x in enumerate(riwayat, start=1):
                            print(f'{i}. Nomor Plat: {x['plat']}\t| Waktu Masuk: {x['waktu_masuk']}\t| Waktu Keluar: {x['waktu_akhir']}\t| Durasi Parkir: {x['durasi']} detik\t| Tagihan: Rp{x['tagihan']}\t| Nominal Pembayaran: Rp{x['nominal']}\t| Kembalian: Rp{x['kembalian']}')
                    elif pilihan == 2:
                        break
                    elif pilihan == 3:
                        quit()
                    elif pilihan == None:
                        pass
                    else:
                        print('Menu yang Anda pilih tidak ada!')
            else:
                print('PIN Admin yang Anda masukan salah!')
        except ValueError:
            print('Tolong masukan angka PIN yang benar!')

    # Fungsi ini digunakan sebagai pengatur jalannya program dan sebagai menu utama. Fungsi dimulai dengan mendefinisikan variable 'pin', variable list 'data_kendaraan', dan variable list 'riwayat_transaksi'. Setelah itu program akan masuk ke perulangan, lalu program akan men-display ucapan selamat datang dan tiga menu. Setelah itu program akan masuk ke fungsi 'pilihan_menu', lalu program meminta pengguna untuk memasukan salah satu nomor menu yang dipilih. Jika pengguna memlihi menu 1, maka program akan masuk ke fungsi 'masuk_kendaraan' dengan memberikan argument list 'data_kendaraan'. Jika pengguna memilih menu 2, maka program akan masuk ke fungsi 'keluar_kendaraan' dengan memberikan argument list 'data_kendaraan' dan list 'riwayat_transaksi'. Jika pengguna memilih menu 3, maka program akan masuk ke 'fungsi admin_parkir' dengan memberikan argument list 'riwayat_transaksi' dan variable 'pin'. Jika pilihan pengguna tidak ada maka program akan men-display 'Menu yang Anda pilih tidak ada!'.
    def main():
        pin = 1234
        data_kendaraan = []
        riwayat_transaksi = []
        while True:
            # print(data_kendaraan)
            # print(riwayat_transaksi)
            print('--- Selamat Datang di Menu Utama ----')
            print('Menu:\n1. Masuk Area Parkir\n2. Keluar Area Parkir\n3. Admin Parkir')
            pilihan = pilihan_menu()
            if pilihan == 1:
                masuk_kendaraan(data_kendaraan)
            elif pilihan == 2:
                keluar_kendaraan(data_kendaraan, riwayat_transaksi)
            elif pilihan == 3:
                admin_parkir(riwayat_transaksi, pin)
            elif pilihan == None:
                pass
            else:
                print('Menu yang Anda pilih tidak ada!')

    if __name__ == '__main__':
        main()
except NameError:
    print('Kesalahan Pemrograman: Variabel yang dipanggil tidak ada pada System')
except ImportError: 
    print('Kesalahan Pemrograman: Modul yang di-import tidak ada')
except ArithmeticError:
    print('Kesalahan Pemrograman: Kesalahan pada perhitungan angka')
except IndexError:
    print('Kesalahan Pemrograman: Index yang dipanggil tidak ada')
except TypeError:
    print('Kesalahan Pemrograman: Tidak bisa menggabungkan dua tipe yang berbeda')
except KeyError:
    print('Kesalahan Pemrograman: Kata kunci tidak ada di dictionary')
except Exception as e:
    print(f'Erorr: {e}')
finally:
    print('=== Program Parkir Selesai ===')