komposisi_nilai = [10/100, 15/100, 10/100, 15/100, 15/100, 15/100, 20/100]
q1, q2, q3, t1, t2, p1, p2 = komposisi_nilai
nilai_mutu = [80.01, 70.01, 65.01, 60.01, 50.01, 40.01, 0]
A, AB, B, BC, C, D, E = nilai_mutu
invalid1 = 100
invalid2 = 0


nq1 = float(input("Masukan Nilai quiz 1 mu: "))
nq2 = float(input("Masukan Nilai quiz 2 mu: "))
nq3 = float(input("Masukan Nilai quiz 3 mu: "))
nt1 = float(input("Masukan Nilai tugas 1 mu: "))
nt2 = float(input("Masukan Nilai tugas 2 mu: "))
np1 = float(input("Masukan Nilai proyek 1 mu: "))
np2 = float(input("Masukan Nilai proyek 2 mu: "))

nilai_akhir = (nq1 * q1 + nq2 * q2 + nq3 * q3 + nt1 *
               t1 + nt2 * t2 + np1 * p1 + np2 * p2)

if nilai_akhir > invalid1 or nilai_akhir < invalid2:
    print("Tolong input nilai dengan benar! Karena nilai anda:", nilai_akhir)
elif nilai_akhir >= A:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: A")
elif nilai_akhir >= AB:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: AB")
elif nilai_akhir >= B:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: B")
elif nilai_akhir >= BC:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: BC")
elif nilai_akhir >= C:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: C")
elif nilai_akhir >= D:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: D")
elif nilai_akhir >= E:
    print("Nilai akhir mu adalah: ", nilai_akhir, "dengan Nilai Mutu: E")
