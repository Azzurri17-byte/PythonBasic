print('.:: KALKULATOR IMT ::.')

def imt():
    gender = input('Laki - laki atau Perempuan? (inputkan L atau P): ')
    if gender == 'L':
        tinggiBadan = float(input('Berapa tinggi badan anda?: '))
        beratBadan = float(input('Berapa berat badan anda?: '))
        TB_meter = tinggiBadan / 100
        TB_kuadrat = TB_meter * TB_meter
        hasilIMT = beratBadan / TB_kuadrat

        if hasilIMT <= 18.6:
            print('BB kurang')
        elif 18.6 <= hasilIMT <= 23.9:
            print('Normal')
        elif 23.9 <= hasilIMT <= 26.7:
            print('Kelebihan BB')
        else:
            print('Obesitas')
    elif gender == 'P':
        tinggiBadan = float(input('Berapa tinggi badan anda?: '))
        beratBadan = float(input('Berapa berat badan anda?: '))
        TB_meter = tinggiBadan / 100
        TB_kuadrat = TB_meter * TB_meter
        hasilIMT = beratBadan / TB_kuadrat
        
        if hasilIMT <= 18.3:
            print('BB kurang')
        elif 18.3 <= hasilIMT <= 23.4:
            print('Normal')
        elif 23.4 <= hasilIMT <= 24.9:
            print('Kelebihan BB')
        else:
            print('Obesitas')
    else:
        print('Mohon inputkan antara L atau P!!')


