meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "BRB": "Be right back"
            }

while True :
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        break
    else :
        print("SORRY! we can't find that word in our dictionary :( ")
  
