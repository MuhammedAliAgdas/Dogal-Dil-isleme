import random
from textblob import TextBlob

csv_path = 'on_islenmis_veriler.csv'  # Dosyanın adını ve yolunu uygun şekilde değiştirin
with open(csv_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

def analiz_et(cumle):
    analiz = TextBlob(cumle)
    return analiz.sentiment.polarity

duygu_polariteleri = [(index, analiz_et(line.strip()), line.strip()) for index, line in enumerate(lines, start=1)]

# En olumlu ve en olumsuz ilk 5 cümleleri bul
en_olumlu_cumleler = sorted(duygu_polariteleri, key=lambda x: x[1], reverse=True)[:5]
en_olumsuz_cumleler = sorted(duygu_polariteleri, key=lambda x: x[1])[:5]
nötr_cumleler = sorted(duygu_polariteleri, key=lambda x: abs(x[1]))[:5]
rastgele_cumleler = random.sample(duygu_polariteleri, 5)

polarity_listesi = [analiz_et(line.strip()) for line in lines]

# Olumlu cümlelerin ve olumsuz cümlelerin sayısını hesapla
olumlu_sayisi = sum(1 for polarite in polarity_listesi if polarite > 0)
olumsuz_sayisi = sum(1 for polarite in polarity_listesi if polarite < 0)
nötr_sayisi = sum(1 for polarite in polarity_listesi if polarite == 0)
toplam_cümle_sayisi = len(polarity_listesi)

# Olumlu cümlelerin duygu yoğunluğu ortalamasını hesapla
olumlu_ortalama = sum(polarite for polarite in polarity_listesi if polarite > 0) / olumlu_sayisi if olumlu_sayisi > 0 else 0

# Olumsuz cümlelerin duygu yoğunluğu ortalamasını hesapla
olumsuz_ortalama = sum(polarite for polarite in polarity_listesi if polarite < 0) / olumsuz_sayisi if olumsuz_sayisi > 0 else 0

# Sonuçları yazdır
print("En Olumlu İlk 5 Cümle:")
for index, duygu_polarity, cumle in en_olumlu_cumleler:
    print(f"Satır {index}: Duygu Yoğunluğu: %{duygu_polarity*100}, Cümle: {cumle}")

print("\nEn Olumsuz İlk 5 Cümle:")
for index, duygu_polarity, cumle in en_olumsuz_cumleler:
    print(f"Satır {index}: Duygu Yoğunluğu: %{abs(duygu_polarity)*100}, Cümle: {cumle}")

print("\nEn Nötr ilk 5 Cümle:")
for index, duygu_polarity, cumle in nötr_cumleler:
    print(f"Satır {index}: Duygu Yoğunluğu: %{duygu_polarity}, Cümle: {cumle}")

print("\nRastgele Seçilen 5 Cümle ve duygu yoğunluğu oranları:")
for index, duygu_polarity, cumle in rastgele_cumleler:
    if duygu_polarity <= 1 and duygu_polarity > (2/3):
        print(f"Satır {index}: Duygu Yoğunluğu: %{duygu_polarity*100} orannda çok olumlu, Cümle: {cumle}")
    elif duygu_polarity > 0 and duygu_polarity < (2/3):
        print(f"Satır {index}: Duygu Yoğunluğu: %{duygu_polarity*100} oranında az olumlu, Cümle: {cumle}")
    elif duygu_polarity >= -1 and duygu_polarity < -(2/3):
        print(f"Satır {index}: Duygu Yoğunluğu: %{abs(duygu_polarity*100)} oranında çok olumsuz, Cümle: {cumle}")
    elif duygu_polarity < 0 and duygu_polarity> -(2/3):
        print(f"Satır {index}: Duygu Yoğunluğu: %{abs(duygu_polarity*100)} oranında az olumlu, Cümle: {cumle}")
    elif duygu_polarity == 0:
        print(f"Satır {index}: Duygu Yoğunluğu: %{duygu_polarity*100}(Nötr), Cümle: {cumle}")

ortalama_duygu_polarity = sum([analiz_et(line.strip()) for line in lines]) / len(lines)
print(" ")
print(" ")
print(f"Olumlu Cümle Yüzdesi: %{(olumlu_sayisi / toplam_cümle_sayisi) * 100}")
print(f"Olumsuz Cümle Yüzdesi: %{(olumsuz_sayisi / toplam_cümle_sayisi) * 100}")
print(f"Nötr Cümle Yüzdesi: %{(nötr_sayisi / toplam_cümle_sayisi) * 100}")

print(f"Olumlu Cümlelerin Duygu Yoğunluğu Ortalaması: {olumlu_ortalama}")
print(f"Olumsuz Cümlelerin Duygu Yoğunluğu Ortalaması: {abs(olumsuz_ortalama)}")
