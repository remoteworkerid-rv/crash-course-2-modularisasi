"""
Program menghitung luas segitiga
Luas Segitiga = alas * tinggi / 2
"""

print('\nMenghitung luas segitiga 1')
alas = 10
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi luas segitiga')


alas = 30
tinggi = 5
print(f'Dengan fungsi ini, segitiga alas={alas} dan tinggi={tinggi} memiliki luas {hitung_luas_segitiga(alas, tinggi)}')
print(f'Menghitung luas segitiga dengan fungsi, Hasilnya = {hitung_luas_segitiga(10,6)}')
print(f'Menghitung luas segitiga dengan fungsi, Hasilnya = {hitung_luas_segitiga(50,2)}')

