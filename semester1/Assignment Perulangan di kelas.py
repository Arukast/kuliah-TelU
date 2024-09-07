# Tb. Alta Ulil Abshor

# Tugas 1
for i in range(0, 5):
    for j in range(0, i + 1):
        print('*', end=' ')
    print('\n')
    
    
    
# Tugas 2
n = 0
m = 0
i = 9
while i > 0:
    print(i)
    n += i
    i -= 2
print(n)


for i in range(1, 10, 2):
    print(i)
    m += i
print(n)


# Tugas 3
baris = 1


while baris <= 5:

    spasi = 5 - baris
    while spasi > 0:
        print(" ", end="")
        spasi -= 1
    karakter = 1
    while karakter <= (2 * baris - 1):
        print("*", end="")
        karakter += 1

    print()
    baris += 1


baris = 4


while baris >= 1:
    spasi = 5 - baris
    while spasi > 0:
        print(" ", end="")
        spasi -= 1

    karakter = 1
    while karakter <= (2 * baris - 1):
        print("*", end="")
        karakter += 1

    print()
    baris -= 1

# Tb. Alta Ulil Abshor