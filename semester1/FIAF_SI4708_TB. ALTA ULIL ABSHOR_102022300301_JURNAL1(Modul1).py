# Jurnal 1
"""Udin berencana untuk mendaftarkan diri sebagai peserta pound fit. Panitia
penyelenggara acara pound fit tersebut mengharuskan Udin untuk
memasukkan beberapa informasi biodata pribadi seperti nama, umur, jenis
kelamin, tinggi badan, dan nomor telepon. Rencananya setelah Udin
memasukkan data tersebut, program akan menampilkan tipe data dari setiap
informasi yang Udin berikan. Panitia acara pound fit meminta bantuanmu
sebagai programmer andal. Buatlah program supaya Udin dapat menginputkan
informasi pribadinya sekaligus menampilkan tipe data tersebut."""

print("=== Tolong Masukan Biodata Anda ===")
nama = input("Masukan nama Anda: ")
umur = int(input("Masukan umur Anda: "))
jenis_kelamin = input("Jenis kelamin: ")
tinggi_badan = float(input("Masukan tinggi badan Anda: "))
nomor_telepon = int(input("Masukan nomor telepon Anda: "))
print("")
print("=== Hasil Biodata ===")
print(f"Nama : {nama}")
print(f"Umur : {umur}")
print(f"Jenis kelamin : {jenis_kelamin}")
print(f"Tinggi Badan : {tinggi_badan}")
print(f"Nomor Telepon : {nomor_telepon}")
print("")
print("=== Tipe Biodata ===")
print(type(nama))
print(type(umur))
print(type(jenis_kelamin))
print(type(tinggi_badan))
print(type(nomor_telepon))
