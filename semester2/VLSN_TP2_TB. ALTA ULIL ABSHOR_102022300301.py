def add_Mahasiswa(dataMahasiswa):
    print('\n--- Menu Menambahkan Data Mahasiswa ---')
    komponen_nilai = ['Nilai Quiz', 'Nilai Tugas', 'Nilai Ujian']
    nama = input('Masukan Nama Mahasiswa: ')
    nim = int(input('Masukan NIM Mahasiswa: '))
    dataMahasiswa[nim] = dict( NIM = nim, Nama = nama)
    for komponen in komponen_nilai:
        dataMahasiswa[nim][komponen] = int(input(f'Masukan {komponen}: '))
    print('\nKonfirmasi data:')
    for data in dataMahasiswa[nim]:
        print(f'{data}: {dataMahasiswa[nim][data]}')
    match input('Apakah data tersebut sudah benar (Ya/Tidak): ').lower():
        case 'ya':
            print('Data mahasiswa berhasil ditambahkan!\n')
            dataMahasiswa[nim]['Nilai Akhir'] = float(f"{((dataMahasiswa[nim]['Nilai Quiz']*0.25)+(dataMahasiswa[nim]['Nilai Tugas']*0.25)+(dataMahasiswa[nim]['Nilai Ujian']*0.5)):.2f}")
        case _:
            print('Penambahan data mahasiswa dibatalkan!\n')
            dataMahasiswa.pop(nim)

def viewData(dataMahasiswa):
    print('\n--- Menu Menampilkan Data Mahasiswa ---\nData Mahasiswa:')
    for i, data in enumerate(dataMahasiswa):
        print(f'{i+1}. NIM: {dataMahasiswa[data]["NIM"]}, Nama: {dataMahasiswa[data]["Nama"]}, Nilai Quiz: {dataMahasiswa[data]["Nilai Quiz"]}, Nilai Tugas: {dataMahasiswa[data]["Nilai Tugas"]}, Nilai Ujian: {dataMahasiswa[data]["Nilai Ujian"]}')
    print()

def hitungNilaiAkhir(dataMahasiswa):
    print('\n--- Menu Hitung Nilai Akhir Mahasiswa ---')
    terpilih = int(input('Masukan NIM mahasiswa yang ingin dihitung Nilai Akhir-nya: '))
    print(f'Nilai akhir dari mahasiswa yang bernama {dataMahasiswa[terpilih]["Nama"]} dengan NIM {dataMahasiswa[terpilih]["NIM"]} adalah: {dataMahasiswa[terpilih]["Nilai Akhir"]}\n')

def urutNilaiAkhir(dataMahasiswa):
    print('\n--- Menu Mengurutkan Data Mahasiswa Berdasarkan Nilai Akhir (dari yang terbesar) ---\nData Mahasiswa:')
    tempData = {}
    for data in dataMahasiswa:
        tempData[data] = dataMahasiswa[data]['Nilai Akhir']
    for i, keys in enumerate(dict(sorted(tempData.items(), key=lambda item: item[1], reverse= True))):
        print(f"{i+1}. NIM: {dataMahasiswa[keys]['NIM']}, Nama: {dataMahasiswa[keys]['Nama']}, Nilai Akhir: {dataMahasiswa[keys]['Nilai Akhir']}")
    print()

def hapusData(dataMahasiswa):
    print('\n--- Menu Hapus Data Mahasiswa ---')
    terpilih = int(input('Masukan NIM mahasiswa yang ingin dihapus datanya: '))
    print(f'Data mahasiswa dengan NIM {dataMahasiswa[terpilih]["NIM"]} berhasil dihapus!\n')
    del dataMahasiswa[terpilih]

def main():
    dataMahasiswa = {}
    while True:
        print('=== Program Managemen Data Mahasiswa DasPro University ===')
        print('Menu Program:\n1. Menambahkan Data Mahasiswa\n2. Menampilkan Seluruh Data Mahasiswa\n3. Menghitung Nilai Akhir\n4. Mengurutkan Data Mahasiswa Berdasarkan Nilai Akhir (dari yang terbesar)\n5. Menghapus Data Mahasiswa\n0. Keluar Program')
        match input('Masukan Nomor Menu Yang Dipilih: '):
            case '1':
                add_Mahasiswa(dataMahasiswa)
            case '2':
                viewData(dataMahasiswa)
            case '3':
                hitungNilaiAkhir(dataMahasiswa)
            case '4':
                urutNilaiAkhir(dataMahasiswa)
            case '5':
                hapusData(dataMahasiswa)
            case '0':
                print('Program Berhenti, Terima Kasih!')
                break
            case _:
                print('Menu yang Anda pilih tidak ada!!!\n')

if __name__ == '__main__':
    main()