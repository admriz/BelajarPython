def input_alas_dan_tinggi  ():
    alas = float(input('masukan alas: '))
    tinggi = float(input('masukan tinggi: '))

    return alas, tinggi

def hitung_luas (alas, tinggi):
    return 0,5 * alas * tinggi

print(hitung_luas(7, 12))