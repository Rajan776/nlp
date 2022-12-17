import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("dog"))
print(wordnet.synset("dog.n.01").lemma_names())
#all lemmas for each synset.
for e in wordnet.synsets("dog"):
 print(f'{e} --> {e.lemma_names()}')
#print all lemmas for a given synset
print(wordnet.synset('dog.n.01').lemmas())
#get the synset corresponding to lemma
print(wordnet.lemma('dog.n.01.dog').synset())
#Get the name of the lemma
print(wordnet.lemma('dog.n.01.dog').name())
#Hyponyms give abstract concepts of the word that are much more specific
#the list of hyponyms words of the computer
syn = wordnet.synset('dog.n.01')
print(syn.hyponyms)
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])
#the semantic similarity in WordNet
vehicle = wordnet.synset('vehicle.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))
