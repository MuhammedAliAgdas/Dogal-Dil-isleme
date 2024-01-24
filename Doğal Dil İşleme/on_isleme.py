import csv
import string
from cleantext import clean
import nltk
from nltk.corpus import stopwords

satirlar = []
stop_words = set(stopwords.words('english'))
sil2  = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "arent", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by","can" ,"cant", "cannot", "could", "couldnt", "did", "didnt", "do", "does", "doesnt", "doing", "dont", "down", "during", "each", "few", "for", "from", "further", "had", "hadnt", "has", "hasnt", "have", "havent", "having", "he", "hed", "hell", "hes", "her", "here", "heres", "hers", "herself", "him", "himself", "his", "how", "hows", "i", "id", "ill", "im", "ive", "if", "in", "into", "is", "isnt", "it", "its", "its", "itself", "lets", "me", "more", "most", "mustnt", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shant", "she", "shed", "shell", "shes", "should", "shouldnt", "so", "some", "such", "than", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "there", "theres", "these", "they", "theyd", "theyll", "theyre", "theyve", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasnt", "we", "wed", "well", "were", "weve", "were", "werent","will" ,"what", "whats", "when", "whens", "where", "wheres", "which", "while", "who", "whos", "whom", "why", "whys", "with", "wont", "would", "wouldnt", "you", "youd", "youll", "youre", "youve", "your", "yours", "yourself", "yourselves","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
with open("veriler.csv", 'r', newline='\r\n', encoding='utf-8') as dosya:
    csv_okuyucu = csv.reader(dosya)

    for satir in csv_okuyucu:
        for cumle in satir:
            cumle= cumle.lower()
            cumle = cumle.translate(str.maketrans("", "", string.punctuation))
            cumle = clean(cumle, no_emoji=True , no_digits=True, no_punct=True)
            kelimeler = cumle.split()
            filtered_kelimeler = [kelime for kelime in kelimeler if kelime.lower() not in stop_words]
            cumle = " ".join(filtered_kelimeler)
            filtered_kelimeler2 = [kelime for kelime in kelimeler if kelime.lower() not in sil2]
            cumle = " ".join(filtered_kelimeler2)
            cumle = cumle.replace("0","")
            cumle = cumle.replace("'","")
            if cumle != "" and len(cumle)>3:
                satirlar.append(cumle[:150])


def son_kelimeyi_sil(cumle):
    kelimeler = cumle.split() 
    if len(kelimeler) > 1:
        return ' '.join(kelimeler[:-1]) 
    else:
        return ""

sonuclar = [son_kelimeyi_sil(cumle) for cumle in satirlar]


with open("on_islenmis_veriler.csv", mode="w", newline="", encoding="utf-8") as dosya:
    csv_writer = csv.writer(dosya)

    for sonuc in sonuclar:
        csv_writer.writerow([sonuc])
