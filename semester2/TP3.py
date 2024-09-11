import pandas as pd

def menu():
    print('Menu Analisis Data:\n1. Tampilkan Keseluruhan Data Frame\n2. 5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi\n3. 5 Kota dengan Tingkat Penganguran Tertinggi\n4. 5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah\n5. 5 Kota dengan Tingkat Pengangguran Terendah\n0. Keluar')

def menu1(dataFrame):
    print(f'\nKeseluruhan Data Frame:\n{dataFrame}')

def menu2(dataFrame):
    dfSubSet = dataFrame[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    print(f'\n5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi:\n{dfSubSet.sort_values(by="Tingkat_Penyelesaian_Pendidikan", ascending=False).head(5)}')

def menu3(dataFrame):
    dfSubSet = dataFrame[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    print(f'\n5 Kota dengan Tingkat Penganguran Tertinggi:\n{dfSubSet.sort_values(by="Tingkat_Setengah_Pengangguran", ascending=False).head(5)}')

def menu4(dataFrame):
    dfSubSet = dataFrame[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    print(f'\n5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah:\n{dfSubSet.sort_values(by="Tingkat_Penyelesaian_Pendidikan", ascending=True).head(5)}')

def menu5(dataFrame):
    dfSubSet = dataFrame[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    print(f'\n5 Kota dengan Tingkat Pengangguran Terendah:\n{dfSubSet.sort_values(by="Tingkat_Setengah_Pengangguran", ascending=True).head(5)}')

def main():
    dataFrame = pd.read_csv('DataPendahuluan.csv')
    while True:
        print()
        menu()
        match input('Masukan angka pilihan menu: '):
            case '1':
                menu1(dataFrame)
            case '2':
                menu2(dataFrame)
            case '3':
                menu3(dataFrame)
            case '4':
                menu4(dataFrame)
            case '5':
                menu5(dataFrame)
            case '0':
                print('Program Berhenti')
                break

if __name__ == '__main__':
    main()