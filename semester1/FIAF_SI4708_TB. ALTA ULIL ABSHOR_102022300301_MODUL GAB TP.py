# Nama: Tb. Alta Ulil Abshor
# NIM: 102022300301
# Soal Nomor 1
try:
    print('=== Kalkulator BMI ===')
    def hitung_bmi(data_pasien):
        print('--- Menu Hitung BMI Pasien ---')
        if len(data_pasien) == 0:
            print('Tidak ada data pasien yang tersedia!')
        else:
            while True:
                print('Daftar pasien:')
                for i, data in enumerate(data_pasien, start=1):
                    print(f'{i}. {data['nama']}\t |{data['beban']} KG\t |{data['tiban']} CM')
                try:
                    pilihan = int(input('Masukan nomor pasien yang ingin dihitung: ')) - 1
                    if 0 <= pilihan < len(data_pasien):
                        try:
                            # data = data_pasien[pilihan]
                            bmi = float('{:.2f}'.format(data_pasien[pilihan]['beban'] / (data_pasien[pilihan]['tiban']/100)**2))
                            if bmi < 18.5:
                                kategori = 'Underweight'
                            elif 18.5 <= bmi <= 24.9:
                                kategori = 'Normal'
                            elif 25 <= bmi <= 29.9:
                                kategori = 'Overweight'
                            elif bmi >= 30:
                                kategori = 'Obesitas'
                            else:
                                pass
                            print(f'{data_pasien[pilihan]['nama']} memiliki BMI {bmi} dan termasuk dalam kategori {kategori}.')
                            break
                        except ZeroDivisionError:
                            print('Terjadi kesalahan: Tinggi Badan tidak boleh sama dengan 0')
                            break
                    else:
                        print('Tolong masukan nomor pasien yang tersedia!\n')
                        continue
                except ValueError:
                    print('Tolong masukan nomor angka pasien!\n')

    def input_data():
        while True:
            try:
                print('--- Menu Input Data Pasien ---')
                nama = input('Masukan nama pasien: ')
                beban = int(input(f'Masukan berat badan pasien {nama} (KG): '))
                tiban = int(input(f'Masukan tinggi badan pasien {nama} (CM): '))
                print('Data telah berhasil dimasukan!')
                return nama, beban, tiban
            except ValueError:
                print('Pada Berat Badan dan Tinggi Badan hanya boleh memasukan bilangan bulat (Integer)!')
                continue

    def main_menu():
        data_pasien = []
        while True:
            try:
                print('\n')
                print('--- Menu Utama ---')
                print('Menu:\n1. Input Data Pasien\n2. Hitung BMI Pasien\n3. Exit')
                x1 = int(input('Pilih Menu (angka menu): '))
                if x1 == 1:
                    print('\n')
                    nama,beban,tiban = input_data()
                    data_pasien.append({
                        'nama' : nama,
                        'beban' : beban,
                        'tiban' : tiban
                    })
                elif x1 == 2:
                    print('\n')
                    hitung_bmi(data_pasien)
                elif x1 == 3:
                    print('Program berakhir, Terima Kasih!')
                    break
                else:
                    print('Pilihan Anda tidak ada, masukan piihan yang valid!')
            except ValueError:
                print('Tolong masukan angka menu!')
                continue
    main_menu()
finally:
    print('=== Program Kalkulator BMI telah selesai ===')

# Soal Nomor 2
try:
    print('=== Kalkulator Pintar ===')
    def masuk_angka():
        x1 = int(input('Masukan angka pertama: '))
        x2 = int(input('Masukan angka kedua: '))
        return x1, x2
    def penjumlahan(angka1, angka2):
        x = angka1 + angka2
        return x
    def pengurangan(angka1, angka2):
        x = angka1 - angka2
        return x
    def perkalian(angka1, angka2):
        x = angka1 * angka2
        return x
    def pembagian(angka1, angka2):
        if angka2 == 0:
            raise ZeroDivisionError('Tidak dapat melakukan pembagian dengan bilangan 0')
        else:
            x = angka1 / angka2
        return x
    def main_kalkulator():
        x1, x2 = masuk_angka()
        print(f'Pilih operasi bilangan:\n\t1. Penjumlahan\n\t2. Pengurangan\n\t3. Perkalian\n\t4. Pembagian')
        y1 = int(input('Masukan operasi bilangan (1-4): '))
        if y1 == 1:
            z1 = penjumlahan(x1, x2)
        elif y1 == 2:
            z1 = pengurangan(x1, x2)
        elif y1 == 3:
            z1 = perkalian(x1, x2)
        elif y1 == 4:
            z1 = pembagian(x1, x2)
        else:
            print('Tolong masukan operasi bilangan yang ada!')
        print(f'Hasil: {z1}')
    main_kalkulator()
except ValueError:
    print('Program ini hanya menerima jenis nilai Integer!')
finally:
    print('Terima kasih sudah menggunakan kalkulator pintar!')
    print('=== Program Kalkulator Pintar telah selesai ===')