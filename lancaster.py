from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
words=['eating','eaten','puts','puting']

for word in words:
        print(word,"---->",lancaster.stem(word))
