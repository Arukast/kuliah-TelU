"""Seorang idol bernama Lucas asal Indonesia sering menggelar konser di Amerika
Serikat. Lucas membutuhkan program untuk menghitung jumlah uangnya
dalam dolar AS. Sebagai asistennya, bantu Lucas untuk membuat program
memasukkan jumlah uang rupiah miliknya lalu mengonversi ke dalam dolar AS.
Asumsikan kurs Rupiah ke Dolar AS (1 Rupiah = 0.00007 Dolar AS)."""

rupiah = float(input("Masukan jumlah uang dalam Rupiah: Rp."))
dollar = rupiah * 0.00007
print(f"Jumlah uang dalam Dollar AS adalah: ${dollar}")
