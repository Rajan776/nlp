from nltk.stem import PorterStemmer
porter=PorterStemmer()
words=['SOLOMON','Connect','Connections','Connected','Connect']

for word in words:
        print(word,"---->",porter.stem(word))
