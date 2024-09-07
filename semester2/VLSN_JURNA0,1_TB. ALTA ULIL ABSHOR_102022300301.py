import pandas as pd

def muat_data():
    # Hint: Isi dengan fungsi untuk memuat data dari file CSV (fungsi untuk membaca data csv?)
    data = pd.read_csv('Proporsi Rumah Tangga Yang Memiliki Akses Terhadap Layanan Sanitasi Layak, 2021-2023.csv')
    return data

def tampilkan_data_frame(data):
    # Hint: Isi dengan fungsi untuk menampilkan seluruh dataframe (print data dari csvnya?)
    print(f'Menampilkan seluruh data:\n{data}')

def tampilkan_gambaran_umum(data):
    # Hint: Isi dengan fungsi untuk menampilkan informasi umum tentang data (print ringkasan statistik deskriptif dari data?)
    print(f'Informasi Data:\n{data.dtypes}\n')
    print(f'Deskripsi Statistik:\n{data.describe()}')

def sepuluh_provinsi_teratas(data):
    # Hint: Isi dengan fungsi untuk menampilkan sepuluh provinsi teratas pada tahun 2023  (pakai sort value)
    x = data[['Provinsi', '2023']]
    prov10Teratas = x.sort_values('2023', ascending=False).head(10)
    print(f'Provinsi 10 teraratas:\n{prov10Teratas}')

def provinsi_dengan_peningkatan_terbesar(data):
    # Hint: Isi dengan fungsi untuk menemukan provinsi dengan peningkatan terbesar dari 2021 ke 2023 (pakai data.loc)
    x = data.loc[data[['2021', '2022', '2023'].idxmax(), 'Provinsi']]
    print(x)

def analisis_korelasi(data):
    # Hint: Isi dengan fungsi untuk menganalisis korelasi antara tahun (fungsi buat mencari korelasi?)
    print(f"Matriks Korelasi:\n{data[['2021', '2022', '2023']].corr()}")
def kinerja_provinsi_tertentu(data, nama_provinsi):
    # Hint: Isi dengan fungsi untuk menampilkan kinerja provinsi tertentu (pakai data.loc dan kondisi jika data tidak ada)
    print(f'{data.loc[data[nama_provinsi]]}')

def utama():
    data = muat_data()
    while True:
        print("=====================================")
        print("Menu Analisis Data:")
        # Hint: Tambahkan pilihan menu sesuai deskripsi soal
        print('1. Tampilkan Seluruh Data\n2. Tampilkan gambaran umum data\n3. Tampilkan 10 provinsi terbaik tahun 2023\n4. Tampilkan provinsi dengan peningkatan terbesar 2021-2023\n5. Analisis korelasi antar tahun\n6. Tampilkan performa provinsis tertentu\n7. Keluar')
        print("=====================================")
        pilihan = int(input("Masukkan pilihan Anda: "))
        # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal
        if pilihan == 1:
            tampilkan_data_frame(data)
        elif pilihan == 2:
            tampilkan_gambaran_umum(data)
        elif pilihan == 3:
            sepuluh_provinsi_teratas(data)
        elif pilihan == 4:
            provinsi_dengan_peningkatan_terbesar(data)
        elif pilihan == 5:
            analisis_korelasi(data)
        elif pilihan == 6:
            nama_provinsi = input('Masukan provinsi pilihan')
            kinerja_provinsi_tertentu(data, nama_provinsi)
        else:
            print('Program berhenti')
            break

if __name__ == "__main__":
    utama()
