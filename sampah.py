import random

def sampah_organik():
    nama_sampah = ['daun', 'Sayur busuk', 'buah busuk',
                   'nasi basi', 'bangkai', 'kotoran hewan',
                   'ranting pohon', 'limbah ternak',
                   'tulang', 'kulit buah', 'cangkang telur']
    
    return random.choice(nama_sampah)

def sampah_anorganik():
    nama_sampah = ['botol plastik', 'karet', 'bungkus plastik',
                   'kardus', 'kresek', 'kotak', 'kertas', 'baterai',
                   'besi', 'kaleng', 'sampah DVD', 'gelas kaca']

    return random.choice(nama_sampah)

def perintah():
    nama_perintah = ['organik', 'anorganik', 'joke', 'Info']

    return (nama_perintah)

def link():
    links = ['https://www.thesca.org/connect/blog/how-recycle-and-why-you-should-do-it/',
             'https://indonesiasustainability.com/pengertian-reduce-reuse-recycle/',
             'https://www.universaleco.id/blog/detail/prinsip-3r-reduce-reuse-dan-recycle/156',
             'https://hyundai.motorstudio.co.id/id/senayan-park/newsrooms/environmental-sustainability',
             'https://icel.or.id/']

    return random.choice(links)


