from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

with open('on_islenmis_veriler.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()



for x in range(5):
# Rastgele bir satır seç
    random_row_index = random.randint(0, len(lines) - 1)
    selected_sentence = lines[random_row_index].strip()

# TfidfVectorizer kullanarak cümleleri vektörleştir
    vectorizer = TfidfVectorizer()
    vectorized_sentences = vectorizer.fit_transform(lines)

# Seçilen cümleyi vektörleştir
    selected_sentence_vector = vectorizer.transform([selected_sentence])

# Cosine similarity kullanarak benzerlikleri ölç
    similarities = cosine_similarity(selected_sentence_vector, vectorized_sentences).flatten()

# Kendi cümlesini hariç en çok benzeyen 3 farklı cümle indeksini bul
    sorted_indices = similarities.argsort()[::-1]  # En yüksek benzerlikten en düşüğüne sırala
    most_similar_indices = [i for i in sorted_indices if i != random_row_index][:3]  # Kendi cümlesini çıkart ve ilk üçü al
    
    print("Teslim edilen derlemdeki {}.cümle: {}".format(random_row_index+1, selected_sentence))
    for i, index in enumerate(most_similar_indices, start=1):
        print("En benzer {}.cümle: {} (Teslim edilen derlemdeki {}.cümle)".format(i,lines[index].strip() ,index+1 ))
    print(" ")
    print("------------------------------------")
    print("------------------------------------")
    print(" ")