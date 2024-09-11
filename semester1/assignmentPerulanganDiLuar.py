buku1 = 5
buku2 = 7
buku3 = 3

while True:
    print(
        f"Daftar buku yang tersedia:\n1. Python Programming ({buku1} tersedia)\n2. Introduction to Science ({buku2} tersedia)\n3. History of World ({buku3} tersedia)"
    )
    x = input(
        'Pilih nomor buku yang ingin dipinjam (atau ketik "selesai" untuk keluar): '
    ).lower()
    if x == "1":
        if buku1 > 0:
            print("Anda telah meminjam buku Python Programming!")
            buku1 -= 1
        else:
            print("Stok buku Python Programming sudah habis!")
    elif x == "2":
        if buku2 > 0:
            print("Anda telah meminjam buku Introduction to Science!")
            buku2 -= 1
        else:
            print("Stok buku Introduction to Science sudah habis!")
    elif x == "3":
        if buku3 > 0:
            print("Anda telah meminjam buku History of World!")
            buku3 -= 1
        else:
            print("Stok buku History of World sudah habis!")
    elif x == "selesai":
        break
    else:
        print("Kami tidak mengerti yang Anda maksud!")
