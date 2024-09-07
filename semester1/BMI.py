berat = float(input("Masukan berat badan anda (dalam KG): "))
tinggi = float(input("Masukan tinggi badan anda (dalam M): "))

hasil = (berat / (tinggi ** 2))
# format_hasil = f"{hasil: .2f}"
print(f"BMI anda: {hasil: .2f}")
if hasil < 17:
    print("Anda dalam kelompok Kurus dengan kategori kekurangan berat badan tingkat berat")
elif hasil >= 17 and hasil <= 18.5:
    print("Anda dalam kelompok Kurus dengan kategori kekurangan berat badan tingkat rendah")
elif hasil >= 18.5 and hasil <= 25:
    print("BMI anda Normal!!")
elif hasil >= 25 and hasil <= 27:
    print("Anda dalam kelompok Gemuk dengan kategori kelebihan berat badan tingkat rendah")
elif hasil > 27:
    print("Anda dalam kelompok Gemuk dengan kategori kelebihan be1rat badan tingkat berat")
