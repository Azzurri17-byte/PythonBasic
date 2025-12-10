# print(".:: Program Bilangan Genap")

# batas = int(input("Batas bilangan genap: "))

# i = 1
# while(i <= batas):
#     if(i % 2 == 0):
#         print(i, end=" ")
#     i += 1

# print('.:: Program daftar perkalian ::.')

# bil = int(input("masukkan bilangan: "))

# i = 1
# while(i <= 10):
#     print(f"{bil} x {i} = {bil*i}")
#     i+= 1

# tebak angka
# import random
# print( ".:: permainan tebak angka ::.")

# komp = random.randint(1,10)
# print('komputer telah memikirkan suatu angka dari 1 - 10. tebak angka tersebut!!')

# kesempatan = 3

# while (kesempatan > 0):
#     angka = int(input("masukkan angka: "))
#     if angka < 1 or angka > 10:
#         print(f'masukkan angka yang benar!!')
#     elif angka == komp:
#             print(f"kamu benar, angkanya adalah = {komp}")
#             kesempatan = 0
#     else:
#         kesempatan -=1
#         if kesempatan == 0:
#               print(f"salah angka sebenarnya adalah {komp}")
#         else:
#              print("tebakan anda salah! coba lagi")
#              print("sisa kesempatan = ", kesempatan)

# kasir
# def kasir():
#     hargaBarang = int(input("Masukkan harga barang: "))
#     jumlahBarang = int(input("Masukkan jumlah harga barang: "))
#     totalBarang = hargaBarang * jumlahBarang

#     if totalBarang >= 100000:
#         print("kamu mendapatkan diskon 10%!")
#         diskonBarang = 10 / 100 * totalBarang
#         diskonBarang = totalBarang - diskonBarang
#         print(f"total belanjaan = {diskonBarang}")
#     else:
#         print(f"total belanjaan = {totalBarang}")

# while True:
#     kasir()
#     restart = input("Ingin mengihtung lagi? (y/n): ").lower()
#     if restart != "y":
#         print("program berakhir...")
#         break


# print(" .:: Program Login Jarvis ::.")

# db = [
#     {
#         "username": "raihan",
#         "password": "12345678"
#     },
#     {
#         "username": "hans",
#         "password": "87654321"
#     },
#     {
#         "username": "jarvis",
#         "password": "1312"
#     }
# ]
# def formLogin():
#     usr = input("Masukkan username anda: ")
#     pw = input("Masukkan password anda: ")

# # for loop untuk membaca key dan value pada dictionary db
# # di dalam for loop tidak disarankan menggunaka else atau elif jadi jika tidak sesuai tunggu sistem loop selesai baru langsung keluar ouputnya
#     for user in db:
#         if usr == user["username"] and pw == user["password"]:
#             print(f"Login berhasil!! Selamat datang {user['username']}")
#             return True
        
# # contoh jika tidak menggunakan else atau elif, konsep sama tapi hemat line
#     print("Username atau password salah!! Coba lagi!!")
#     return False

# # program pengulangan sistem jika user dan pw nya salah
# while True:
#     if formLogin():
#         break
#     restart = input("Isi ulang data form (y/n): ")
#     if restart != "y".lower():
#         break

# print(".:: Program Bilangan Ganjil Dan Jumlahnya ::.")

# batas = int(input("Batas atas bilangan ganjil: "))
# print("Bilangan Ganjil: ", end= "")
# sum = 0 
# for i in range(batas+1):
#     if(i % 2 == 1):
#         print(i, end="" + " ")
#         sum+=i

# print("\n Jumlah: ", sum)

# print(" .:: Program Bilangan Penjumlahan 5 Bilangan Positif ::. \n")

# sum = 0
# for i in range(5):
#     n = float(input(f"bilangan ke-{i+1} : "))
#     if (n <= 0):
#         continue
#     sum += n
# print("Hasil penjumlahan : ", sum)

# print(" .:: Program Segitiga Siku Siku ::.")

# n = int(input("Masukkan Sisi: "))

# for i in range(n):
#     for j in range(i+1):
#         print("x", end="")
#     print()
