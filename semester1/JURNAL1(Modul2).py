total_belanja = int(input("Masukan total belanjaan Anda: Rp."))
program_loyalitas = input(
    "Apakah Anda adalah anggota program loyalitas? (ya/tidak): ")

if total_belanja >= 500000:
    if program_loyalitas == "ya":
        diskon = (total_belanja * 0.2)
        diskon1 = total_belanja * 0.05
        akhir = total_belanja - diskon - diskon1
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
    else:
        diskon = total_belanja * 0.2
        akhir = total_belanja - diskon
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
elif total_belanja >= 300000 and total_belanja < 500000:
    if program_loyalitas == "ya":
        diskon = (total_belanja * 0.15)
        diskon1 = total_belanja * 0.05
        akhir = total_belanja - diskon - diskon1
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
    else:
        diskon = total_belanja * 0.15
        akhir = total_belanja - diskon
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
elif total_belanja >= 200000 and total_belanja < 300000:
    if program_loyalitas == "ya":
        diskon = (total_belanja * 0.10)
        diskon1 = total_belanja * 0.05
        akhir = total_belanja - diskon - diskon1
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
    else:
        diskon = total_belanja * 0.10
        akhir = total_belanja - diskon
        print(f"Total belanjaan setelah diskon: Rp.{akhir}")
