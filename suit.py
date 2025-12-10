import random, sys

print('.:: PERMAINAN SUIT/Pingsuit ::.')

print('1. Jempol(Gajah)')
print('2. Telunjuk(Manusia)')
print('3 Kelingking(Semut)')
pil = int(input('Pilihan anda ?: '))
if (pil < 1 or pil > 3):
    sys.exit('Masukkan pilihan yang benar!! Pilhan antara 1 - 3.')
#pilihan komputer
kom = random.randint(1,3)
if kom == 1:
    if pil == 1:
        print('Sama-sama Gajah harus saling membantu...')
    if pil == 2:
        print('Diinjek Gajah kamu kalah!')
    if pil == 3:
        print('Kamu gigit Gajah, kamu menang!')
if kom == 2:
    if pil == 1:
        print('Kamu abis nginjek manusia, kamu menang!')
    if pil == 2:
        print('Sama-sama Manusia! Jangan berantem lah...')
    if pil == 3:
        print('Kamu dibunuh manusia, kamu kalah!')
if kom == 3:
    if pil == 1:
        print('Kamu abis dikerjain sama semut, kamu kalah!')
    if pil == 2:
        print('Kamu ga sengaja injek semut, kamu menang')
    if pil == 3:
        print('Sesama semut saling membahu....')
