import sqlite3
import matplotlib.pyplot as plt

DATABASE_FILE = "karakter_anime.sqlite3"

def create_table():
    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    # Buat kode untuk membuat tabel anime pada database karakter_anime.sqlite3
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tabel_anime(id INTEGER NOT NULL, nama TEXT NOT NULL, anime TEXT NOT NULL, power_level INTEGER NOT NULL, health INTEGER NOT NULL)")
    conn.commit()
    cur.close()

def insert_character(id, nama, anime, power_level, health):
    """Menyisipkan karakter baru ke dalam database
    Args:
        nama: str, nama karakter
        anime: str, judul anime
        power_level: float, tingkat kekuatan karakter
        health: int, tingkat kesehatan karakter
    Output: Success message
    Returns: None
    """
    # Buat kode untuk memasukkan 4 karakter legendaris secara otomatis ke dalam tabel anime
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("INSERT INTO tabel_anime(id, nama, anime, power_level, health) VALUES(?, ?, ?, ?, ?)", (id, nama, anime, power_level, health))
    conn.commit()
    print('Karakter berhasil ditambahkan ke database!')
    cur.close()

def select_all_characters():
    """Mengambil dan mencetak semua karakter dari database
    Args: None
    Output: Informasi karakter dalam database
    Returns: None
    """
    # Buat kode untuk menampilkan isi dari semua tabel anime
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tabel_anime")
    res = cur.fetchall()
    cur.close()
    return res

def simulate_battle(character_id, enemy_id):
    """Mensimulasikan pertempuran antara karakter dengan musuh
    Args:
        character_id: int, id karakter yang menyerang
        enemy_id: int, id musuh yang diserang
    Output: Hasil pertempuran
    Returns: None
    """
    # Buat kode untuk mengambil informasi karakter yang menyerang (character_id) dan musuh yang diserang (enemy_id)
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tabel_anime WHERE id = ?", (character_id,))
    menyerang = cur.fetchone()
    cur.execute("SELECT * FROM tabel_anime WHERE id = ?", (enemy_id,))
    diserang = cur.fetchone()
    cur.close()

    # Mengurangi health musuh berdasarkan power level karakter
    
    health_baru = diserang[4] - menyerang[3]

    # Buat kode untuk mengupdate kesehatan musuh dalam database setelah
    conn = sqlite3.connect('karakter_anime.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE tabel_anime SET health = ? WHERE id = ?", (health_baru, diserang[0]))
    conn.commit()
    cur.close()

    # print hasil pertempuran
    print(f"{menyerang[1]} menyerang {diserang[1]}!, {diserang[1]}'s health berkurang menjadi {health_baru}")



def visualize_health():
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

    # Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.
    data = select_all_characters()
    nama = [nama[1] for nama in data]
    health = [health[4] for health in data]
    plt.figure(figsize=(10, 6))
    plt.bar(nama, health, color='skyblue')
    plt.xlabel('Nama Karakter')
    plt.ylabel('Health')
    plt.title('Kesehatan Karakter Setelah Pertempuran')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan
create_table()
insert_character(1, 'Son Goku', 'Dragon Ball', 5000, 10000)
insert_character(2, 'Naruto Uzumaki', 'Naruto', 4000, 7500)
insert_character(3, 'Monkey D. Luffy', 'One Piece', 3000, 6000)
insert_character(4, 'Icigo Kurosaki', 'Bleach', 3500, 5000)
select_all_characters()
simulate_battle(1, 2)
simulate_battle(2, 1)
simulate_battle(3, 4)
simulate_battle(4, 3)
visualize_health()