def cekData(username, password):
    if username == 'Daspro' and password == 'ALPROASIK':
        indikator = True
        ucapan = 'Selamat, Anda berhasil login!'
    elif username != 'Daspro' and password == 'ALPROASIK':
        indikator = False
        ucapan = 'Username Anda salah, Login gagal!'
    elif username == 'Daspro' and password != 'ALPROASIK':
        indikator = False
        ucapan = 'Password Anda salah, Login gagal!'
    elif username != 'Daspro' and password != 'ALPROASIK':
        indikator = False
        ucapan = 'Username dan password Anda salah, Login gagal!'
    return indikator, ucapan

n = 3

while n > 0:
    username = input('Masukan username Anda: ')
    password = input('Masukan password Anda: ')
    indikator, ucapan = cekData(username, password)
    if indikator == True:
        print(ucapan)
        break
    else:
        n -= 1
        print(ucapan)
        if n > 0:
            print(f'Percobaan tersisa {n} kali!')
        else:
            print('Coba lagi besok!')