def memasukan_nilai(nilai):
    print('\n--- Menu Input Nilai ---')
    kuis = int(input('Masukan nilai Kuis: '))
    nilai['Kuis'] = kuis
    tugas = int(input('Masukan nilai Tugas: '))
    nilai['Tugas'] = tugas
    uts = int(input('Masukan nilai UTS: '))
    nilai['UTS'] = uts
    uas = int(input('Masukan nilai UAS: '))
    nilai['UAS'] = uas
    print('Nilai berhasil dimasukan!\n')
    return nilai
    
def menampilkan_nilai(nilai):
    print('\n--- Menu Data Nilai ---')
    for x in nilai:
        print(f'Nilai {x}: {nilai[x]}')
    print()
    
def menghitung_nilai(nilai):
    print('\n--- Menu Nilai Akhir ---')
    nilai_akhir = float('{:.1f}'.format((0.2 * nilai['Kuis'])+(0.15 * nilai['Tugas'])+(0.3 * nilai['UTS'])+(0.35 * nilai['UAS'])))
    print(f'Nilai Akhir: {nilai_akhir}')
    if nilai_akhir > 80:
        indeks = 'A'
    elif 70 < nilai_akhir <= 80:
        indeks = 'AB'
    elif 65 < nilai_akhir <= 70:
        indeks = 'B'
    elif 60 < nilai_akhir <= 65:
        indeks = 'BC'
    elif 50 < nilai_akhir <= 60:
        indeks = 'C'
    elif 40 < nilai_akhir <= 50:
        indeks = 'D'
    elif nilai_akhir <= 40:
        indeks = 'E'
    else:
        pass
    print(f'Indeks Huruf: {indeks}\n')
    return indeks

def status_kelulusan(indeks):
    print('\n--- Menu Status Kelulusan ---')
    if indeks != 'E':
        print('Status Kelulusan: Lulus')
    else:
        print('Status Kelulusan: Tidak Lulus')
    print()
    
def main():
    print('=== Program TP 1 Berjalan ===')
    komponen_nilai = {
        'Kuis' : 0,
        'Tugas' : 0,
        'UTS' : 0,
        'UAS' : 0
    }
    while True:
        print('--- Main Menu ---')
        print('Menu:\n1. Memasukan Nilai (Kuis, Tugas, UTS, UAS)\n2. Menampilkan Nilai\n3. Menghitung Nilai Akhir\n4. Menampilkan Status Kelulusan\n5. Keluar Program')
        match input('Pilihan Menu (Masukan Nomor Menu): '):
            case '1':
                memasukan_nilai(komponen_nilai)
            case '2':
                menampilkan_nilai(komponen_nilai)
            case '3':
                indeks = menghitung_nilai(komponen_nilai)
            case '4':
                status_kelulusan(indeks)
            case '5':
                print('Program berhenti. Terima kasih telah menggunakan program ini :)')
                print('=== Program TP 1 Berhenti ===')
                break
            case _:
                print('Invalid INPUT!\n')

if __name__ == '__main__':
    main()