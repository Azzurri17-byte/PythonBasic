import math

print('.:: PROGRAM LUAS BIDANG ::.\n')
print('1. Persegi')
print('2. Persegi panjang')
print('3. Lingkaran')
pil = int(input('Pilihan anda? '))

if pil == 1:
    sisi = float(input('Berapa sisi persegi? '))
    luasPersegi = sisi * sisi
    print('luas persegi = ', luasPersegi)
elif pil == 2 :
    panjang = float(input('Berapa panjang persegi panjang? '))
    lebar = float(input('Berapa lebar persegi? '))
    luasPersegiPanjang = panjang * lebar
    print('Luas persegi panjang = ', luasPersegiPanjang)
elif pil == 3:
    r = float(input('Berapa jari-jari lingkaran? '))
    phi = 3.14
    luasLingkaran = phi * r**2
    print('Luas lingkaran = ', luasLingkaran, 'cm**2')
else:
    print('Tolong inputkan nomor dari 1 - 3')