nama = 'Ratri Ismawati'
program = 'Gerak Lurus'

print(f'program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'Jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

def hitung_daya(usaha, waktu):
    daya = usaha / waktu
    print(f'usaha = {usaha * 2000}joule ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga daya = {daya} J/s')
    return daya

# usaha = 2000
# waktu = 4 * 60
daya = hitung_daya(2000, 4 * 60)
daya = hitung_daya(1000, 60 * 60)

