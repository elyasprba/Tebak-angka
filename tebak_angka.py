from random import randint

#Tampilan awal saat program jalan
print('*' * 50)
print('PERMAINAN TEBAK ANGKA')
print('*' * 50)

# Inisialisai
angka = randint(1,50)
kesempatan = 10
ulang = True

print('Pikirkan angka dari 1 - 50 ')
print('Silahkan tebak angka yang program pikirkan')
print('Input harus berupa angka!')

while ulang:
    print(f'Kesempatan kamu saat ini tinggal {kesempatan}')
    if kesempatan > 0:
        tebak = input('Masukan tebakan kamu : ')
        if tebak.isnumeric():
            tebak = eval(tebak)
            if tebak > angka:
                kesempatan -= 1
                print('Tebakan anda terlalu besar, kesempatan kamu dikurangi 1')
            elif tebak < angka:
                kesempatan -= 1
                print('Tebakan kamu terlalu kecil, kesempatan kamu dikurangi 1 ')
            else:
                print('Selamat!, Tebakan kamu benar')
                print(f'Kesempatan kamu {kesempatan}')
                ulang = False
            print()
        else:
            kesempatan -= 2
            print('')
            print('[BODOH KAMU] UDAH DIBILANG HARUS ANGKA! JANGAN BATU!!!')
            print('Karna kamu tidak membaca intruksi awal maka kesempatan kamu dikurangi 2')
        print()
    else:
        print()
        print('GAME SELESAI')
        print(f'Kesempatan kamu sisa {kesempatan}')
        ulang = False

