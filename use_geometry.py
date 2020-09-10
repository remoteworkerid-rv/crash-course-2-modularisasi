# import geometri.segitiga as gs
from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f'luas segitiga adalah {hitung_luas_segitiga(10,5)}\n')
print(info_persegipanjang())
print(f'luas persegi panjang adalah {hitung_luas_persegi_panjang(11,5)}')