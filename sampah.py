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

