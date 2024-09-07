print('=== Tugas Pendahuluan 1 ===')
'''Bapak Gunawan merupakan seorang guru di salah satu sekolah dasar. Hari ini dia diminta untuk menghitung rata rata
nilai matematika dari siswa di kelasnya. Untuk mempermudah Bapak Gunawan menghitung rata-rata nilai siswa dikelasnya,
Bapak Gunawan meminta bantuanmu untuk membuatkan sebuah program yang bisa menginputkan jumlah siswa dan
memasukkan nilai satu demi satu dari angka yang telah dimasukkan.
Hint:
 Gunakan input untuk menentukan jumlah siswa, percabangan, for loop.
Contoh:
 Ketika Bapak Gunawan memasukkan jumlah siswa 5, maka program akan meminta Bapak Gunawan untuk memasukkan
 jumlah siswa sebanyak 5 kali. Apabila Bapak Gunawan menginputkan angka tidak pada rentang 0-100 maka program akan
 menampilkan pesan error "Gagal! Mohon masukkan nilai dari rentang 0-100!" dan program akan berakhir.
Dari contoh di atas, buatlah program tersebut dalam bahasa Python!'''
print('--- Program menghitung rata-rata nilai ---')
jumlah_siswa = int(input('Masukan jumlah siswa: '))
rata_rata = 0
for x1 in range(jumlah_siswa):
    x1 = int(input(f'Masukan nilai ke-{x1+1}: '))
    if 0 <= x1 <= 100:
        rata_rata += x1
    else:
        print('Gagal! Mohon masukkan nilai dari rentang 0-100!')
        break
else:
    print(f'Rata-rata nilai = {rata_rata / jumlah_siswa}')
# y1 = 0
# while jumlah_siswa > 0:
#     y1 += 1
#     x1 = int(input(f'Masukan nilai ke-{y1}: '))
#     if 0 <= x1 <= 100:
#         rata_rata += x1
#         jumlah_siswa -= 1
#     else:
#         print('Gagal! Mohon masukkan nilai dari rentang 0-100!')
#         break
# print(f'Rata-rata nilai = {rata_rata / y1}')

print('=== Tugas Pendahuluan 2 ===')
'''Roni adalah karyawan di perusahaan X. Ketika awal bulan Roni mendapatkan gaji dan ingin menabungnya, Roni ingin
menghitung berapa jumlah uang yang akan Roni tabung setiap bulan selama beberapa bulan ke depan hingga Roni bisa
mencapai nominal yang diinginkan. Roni meminta bantuanmu untuk dibuatkan program yang dapat menentukan berapa
nominal yang harus ditargetkan Roni selama menabung dan menginputkan nominal yang ingin ditabung Roni setiap
bulannya.
Hint:
 Gunakan input dan while loop untuk memasukkan jumlah uang dan bulan, gunakan percabangan untuk menentukan
 apakah sudah mencapai tujuan atau belum.
Contoh:
 Ketika Roni menargetkan ingin menabung sebesar 1.000.000 selama 10 bulan, maka program akan meminta
 Roni untuk memasukkan uang sebanyak 10 kali. Jika selama 10 bulan Roni telah menabung sesuai
 dengan target yang ditentukan maka program akan menampilkan pesan "Anda telah berhasil menabung sesuai target!"
 lalu menampilkan total tabungan Roni, namun ketika belum mencapai target maka program akan menampilkan
 kekurangan dari jumlah target yang ditentukan sebelumnya lalu menampilkan total tabungan Roni.
Dari contoh di atas, buatlah program tersebut dalam bahasa Python!'''
print('--- Program Target menabung ---')
x2 = int(input('Masukan nominal yang diinginkan: Rp. '))
y2 = int(input('Masukan jangka waktu (Bulan): '))
counter_2 = 1
total_akhir2 = 0
while y2 > 0:
    tabungan = int(
        input(f'Masukan uang tabungan di bulan ke-{counter_2}: Rp. '))
    total_akhir2 += tabungan
    counter_2 += 1
    y2 -= 1
else:
    if total_akhir2 >= x2:
        print(f'Anda telah berhasil menabung sesuai target!')
        print(f'Tabungan Anda sekarang sebesar Rp. {total_akhir2}')
    else:
        print(f'Tabungan Anda kurang Rp. {x2 - total_akhir2} dari Rp. {x2}')
        print(
            f'Tabungan Anda sekarang sebesar Rp. {total_akhir2}, silahkan menabung lagi!')
