muatan = int(input("Masukan berat muatan (Ton): "))
penumpang = int(input("Masukan jumlah penumpang: "))

if penumpang <= 5 and muatan <= 1:
    print("Kendaraan yang sesuai: Mobil")
elif penumpang <= 40 and muatan <= 5:
    print("Kendaraan yang sesuai: Bus")
elif penumpang == 0 and muatan <= 20:
    print("Kendarann yang sesuai: Truk")
else:
    print("Tidak ada kendaraan yang sesuai")
