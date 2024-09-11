import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def pilih_menu():
    print('Menu:\n1. Buat Tabel\n2. Masukkan Buku\n3. Tampilkan Buku\n4. Hapus Buku\n5. Tampilkan Data\n6. keluar')
    return input('pilih Menu: ')

def membuat_table():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    print('Database berhasil dibuat!')
    cur.execute('CREATE TABLE IF NOT EXISTS tabel_buku(id_buku INTEGER PRIMARY KEY AUTOINCREMENT, judul TEXT NOT NULL, penulis TEXT NOT NULL, tahun_terbit INTEGER, genre TEXT, stok INTEGER NOT NULL)')
    print('Tabel berhasil dibuat!\n')
    conn.commit()
    conn.close()
    
def memasukan_data(judul, penulis, tahun_terbit, genre, stok):
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO tabel_buku(judul, penulis, tahun_terbit, genre, stok) VALUES(?, ?, ?, ?, ?)', (judul, penulis, tahun_terbit, genre, stok))
    conn.commit()
    conn.close()
    
def memasukan_data_input():
    while True:
        judul = input('Masukkan judul buku: ')
        if not judul:
            print('\nMenu memasukkan data buku berhenti!\n')
            break
        penulis = input('Masukkan nama penulis: ')
        tahun_terbit = input('Masukkan tahun terbit: ')
        genre = input('Masukkan genre buku: ')
        stok = input('Masukkan jumlah stok buku: ')
        memasukan_data(judul, penulis, tahun_terbit, genre, stok)
        print(f'\nBuku "{judul}" telah ditambahkan ke dalam database!\n')

def membaca_tabel_buku():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM tabel_buku')
    result = cur.fetchall()
    conn.close()
    return result

def menampilkan_tabel_buku():
    tabel_buku = PrettyTable()
    tabel_buku.field_names = ['ID', 'Judul', 'Penulis', 'Tahun Terbit', 'Genre', 'Stok']
    for baris in membaca_tabel_buku():
        tabel_buku.add_row(baris)
    return tabel_buku


def menghapus_data():
    id_buku = int(input('Masukan ID buku yang ingin dihapus: '))
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM tabel_buku WHERE id_buku=?', (id_buku,))
    conn.commit()
    conn.close()
    print(f'\nBuku dengan ID {id_buku} telah dihapus dari database!\n')

def stok_groupby_genre():
    conn = sqlite3.connect('inventaris_buku.db')
    cur = conn.cursor()
    cur.execute('''
                SELECT genre, SUM(stok) as total_stok
                FROM tabel_buku
                GROUP BY genre
                ''')
    result = cur.fetchall()
    conn.close()
    return result

def visualisasi_data():
    data = stok_groupby_genre()
    genre = [baris[0] for baris in data]
    jumlah_buku = [baris[1] for baris in data]
    plt.figure(figsize=(10, 6))
    plt.bar(genre, jumlah_buku, color='skyblue')
    plt.xlabel('Genre')
    plt.ylabel('Jumlah Buku')
    plt.title('Inventaris Jumlah Buku Berdasarkan Genre')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    print('Visualisasi data sudah ditampilkan!\n')

def main():
    while True:
        match pilih_menu():
            case '1':
                membuat_table()
            case '2':
                memasukan_data_input()
            case '3':
                print(f'Menampilkan Tabel Buku:\n{menampilkan_tabel_buku()}\n')
            case '4':
                menghapus_data()
            case '5':
                visualisasi_data()
            case '6':
                print('Program Berhenti!\n')
                break
            case _:
                print('Masukan nomor menu yang terdapat pada Menu!\n')

if __name__ == '__main__':
    main()