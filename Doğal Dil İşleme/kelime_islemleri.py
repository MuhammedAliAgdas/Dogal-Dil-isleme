from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

model_path = 'GoogleNews-vectors-negative300.bin'
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)


def find_similar_words(word, topn=5):
    # Belirli bir kelimenin en yakın kelimelerini bulma
    similar_words = word2vec_model.most_similar(word, topn=topn+15)  # Daha fazla benzer kelime al

    # Filtreleme adımları
    similar_words = [(w.lower(), s) for w, s in similar_words if '_' not in w and "'" not in w]

    unique_similar_words = []
    added_words = set()

    for w, s in similar_words:
        lowercase_w = w.lower()

        if lowercase_w != word.lower() and lowercase_w not in added_words:
            unique_similar_words.append((w, s))
            added_words.add(lowercase_w)

        if len(unique_similar_words) >= topn:
            break

    # Eğer istenen benzer kelime sayısına ulaşılamazsa, başka benzer kelimelerle doldur
    while len(unique_similar_words) < topn:
        additional_similar_words = word2vec_model.most_similar(word, topn=topn*2)
        additional_similar_words = [(w.lower(), s) for w, s in additional_similar_words if '_' not in w and "'" not in w]
        unique_similar_words.extend(additional_similar_words)
        added_words.update(w[0] for w in additional_similar_words)
        
    return unique_similar_words[:topn]

# CSV dosyasını oku (sütun adları yoksa)
dosya_yolu = 'on_islenmis_veriler.csv'  # Dosya yolunu kendi dosya yolunuzla değiştirin
veri = pd.read_csv(dosya_yolu, header=None)

# Tüm cümleleri birleştir )
tum_cumleler = ' '.join(str(cumle) for cumle in veri.iloc[:, 0])

# Küçük harfe çevir ve kelimelere ayır
kelimeler = word_tokenize(tum_cumleler.lower())

# İngilizce stopwords listesini kullanarak stopwords'leri kaldır ve son harfi 's' olan kelimeleri filtrele
stop_words = set(stopwords.words('english'))
kelimeler = [kelime for kelime in kelimeler if kelime.isalpha() and kelime not in stop_words and not kelime.endswith('s') and kelime != "shawshank"]

# Kelimelerin frekansını say
kelime_frekans = Counter(kelimeler)

# En sık kullanılan 20 kelimeyi bul
en_sik_kelimeler = kelime_frekans.most_common(20)

# Sonuçları ekrana yazdır
for kelime, frekans in en_sik_kelimeler:
    print(f'Kelime: {kelime}, Derlemde kaç tane var: {frekans}')
    similar_words = find_similar_words(kelime)
    for i, (similar_word, similarity) in enumerate(similar_words, 1):
        print(f"{i}. Benzer Kelime: {similar_word}")