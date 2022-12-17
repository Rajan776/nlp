from nltk.stem import PorterStemmer
porter=PorterStemmer()
words=['YASEERA','Connect','Connecting','Connections','Connected','Connect']

for word in words:
  print(word,"----->",porter.stem(word))
