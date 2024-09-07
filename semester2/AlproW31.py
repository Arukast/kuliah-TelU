import array as larik
var_arr = larik.array("i", [301, 302, 303, 304, 305, 306, 307, 308, 309])

def nambah():
    y = int(input('Masukan nim yang ingin ditambah: '))
    var_arr.append(y)

def menghapus():
    z = int(input('Masukan index nim yang ingin di hapus: '))
    del(var_arr[z])
    
def memodifikasi():
    k = int(input('Masukan index nim yang ingin di ubah: '))
    l = int(input('Masukan nomor nim: '))
    var_arr[k] = l
    
def slicing():
    x = int(input('Masukan batas awal: '))
    y = int(input('Masukan batas akhir: '))
    print(var_arr[x:y])
    
    
while True:
    print("Absen:")
    for i in range(len(var_arr)):
        print(var_arr[i], end=" ")
    print()
    x = input('Masukan Menu: ')
    if x == '1':
        nambah()
    elif x == '2':
        menghapus()
    elif x == '3':
        memodifikasi()
    elif x == '4':
        slicing()
    else:
        break
