#import library sqlite 3 dan maplotlib
import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#buatlah database yang dapat diakses secara keseluruhan

#Buatlah fungsi untuk membuat tabel
def buattabel(): 
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS daftar_obat(
                    id_obat INTEGER PRIMARY KEY,
                    nama TEXT NOT NULL,
                    harga INTEGER NOT NULL,
                    stok INTEGER NOT NULL,
                    jenis_obat TEXT NOT NULL
                )
                """)
    conn.commit()
    print('Tabel berhasil dibuat')
    conn.close()

#Buatlah fungsi untuk menambahkan obat
def tambah_obat(id_obat, nama, harga, stok, jenis_obat):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO daftar_obat(id_obat, nama, harga, stok, jenis_obat) VALUES(?, ?, ?, ?, ?)", (id_obat, nama, harga, stok, jenis_obat))
    conn.commit()
    print('Obat berhasil ditambahkan!')
    conn.close()

#Buatlah fungsi untuk hapus obat berdasarkan id obat
def hapus_obat(id_obat):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("""DELETE FROM daftar_obat WHERE id_obat=?""", (id_obat,))
    conn.commit()
    print('Obat berhasil dihapus!')
    conn.close()

#Buatlah fungsi untuk mencari obat berdasarkan id
def cari_obat(id_obat : int):
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM daftar_obat WHERE id_obat=?""", (id_obat,))
    res = cur.fetchall()
    conn.close()
    return res


#Buatlah fungsi untuk menampilkan seluruh obat yang ada pada tabel
def tampilkan_obat():
    conn = sqlite3.connect('database_obat.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM daftar_obat""")
    res = cur.fetchall()
    conn.close()
    return res
#Buatlah fungsi untuk visualisasi data dalam bentuk bar chart
def vis_data():
    data = tampilkan_obat()
    nama = [nama[1] for nama in data]
    stok = [stok[3] for stok in data]
    plt.figure(figsize=(10, 6))
    plt.bar(nama, stok, color='blue')
    plt.xlabel('Nama Obat')
    plt.ylabel('Stok Obat')
    plt.title('Stok Keseluruhan Obat')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

#buatlah perulangan untuk menampilkan pilihan menu dan menjalankan program
while True:
    #Tampilkan menu
    print('Pilihan Menu:\n1. Membuat Tabel\n2. Menambah Obat\n3. Menghapus Obat\n4. Mencari Obat\n5. Menampilkan Data\n6. Visualisasi Data\n7. Keluar')
    pilihan = int(input("Masukan pilihan menu: "))
    if pilihan == 1:
        buattabel()
    elif pilihan == 2:
        id_obat = int(input('Masukan ID obat: '))
        nama = input('Masukan nama obat: ')
        harga = int(input('Masukan harga obat: '))
        stok = int(input('Masukan stok obat: '))
        jenis_obat = input('Masukan jenis obat: ')
        tambah_obat(id_obat, nama, harga, stok, jenis_obat)
    elif pilihan == 3:
        id_obat = int(input('Masukan ID obat yang ingin dihapus: '))
        hapus_obat(id_obat)
    elif pilihan == 4:
        id_obat = int(input('Masukan ID obat yang ingin dicari: '))
        res = cari_obat(id_obat)
        table = PrettyTable()
        table.field_names = ['id_obat', 'nama', 'harga', 'stok', 'jenis_obat']
        for row in res:
            table.add_row(row)
        print(table)
    elif pilihan == 5:
        res = tampilkan_obat()
        table = PrettyTable()
        table.field_names = ['id_obat', 'nama', 'harga', 'stok', 'jenis_obat']
        for row in res:
            table.add_row(row)
        print(table)
    elif pilihan == 6:
        vis_data()
    elif pilihan == 7:
        print('Program Berhenti')
        break
    else :
        print('Pilih Menu yang tersedia!')