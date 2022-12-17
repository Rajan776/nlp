from nltk.stem import SnowballStemmer
snowball=SnowballStemmer(language="english")
words=['SOLOMON','Generous','Generate','Generation','Generously']

for word in words:
        print(word,"---->",snowball.stem(word))
