print(" .:: Program Menghitung Gaji Karyawan ::. ")
def program_gaji():
    gaji = 3700000
    nama_karyawan = input("Masukkan nama karyawan: ")
    ketidakhadiran = int(input("Masukkan ketidakhadiran karyawan: "))

    denda = (1 / 100) * ketidakhadiran * gaji
    bonus = (20 / 100) * gaji
    hasil_bonus = gaji + bonus
    hasil_denda = gaji - denda

    if ketidakhadiran == 0:
        print(f"\nNama karyawan {nama_karyawan} dengan jumlah ketidakhadiran {ketidakhadiran} "
              f"mendapat gaji sebesar Rp.{gaji:,.0f} + bonus Rp.{bonus:,.0f} = Rp.{hasil_bonus:,.0f}")
    elif ketidakhadiran > 0:
        izin = input("Apakah karyawan izin? (y/n): ").lower()
        if izin == "y":
            total_izin = int(input("Berapa total izin karyawan tahun ini?: "))
            if total_izin + ketidakhadiran <= 12:
                print(f"\nNama karyawan {nama_karyawan} mendapat gaji tetap sebesar Rp.{gaji:,.0f}")
            elif total_izin + ketidakhadiran > 12:
                batas_izin = total_izin + ketidakhadiran - 12
                denda = (1 / 100) * batas_izin * gaji
                denda_batas_izin = gaji - denda
                print(f"\nNama karyawan {nama_karyawan} melebihi batas izin sebanyak {batas_izin} hari.")
                print(f"Gaji Rp.{gaji:,.0f} - Denda Rp.{denda:,.0f} = Rp.{denda_batas_izin:,.0f}")
        else:
            print(f"\nNama karyawan {nama_karyawan} dengan jumlah ketidakhadiran {ketidakhadiran} "
                  f"mendapat gaji Rp.{gaji:,.0f} - denda Rp.{denda:,.0f} = Rp.{hasil_denda:,.0f}")

    return True


while True:
    if program_gaji():
        while True:
            restart = input("\nLanjut program? (y/n): ").lower()
            if restart == "y":
                break
            elif restart == "n":
                print("\nTerima kasih! Program selesai.")
                exit()
            else:
                print("Input tidak valid")
