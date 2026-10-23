import nltk
nltk.download("wordnet")

from nltk.corpus import wordnet

word = "book"
synsets = wordnet.synsets(word)

for synset in synsets[:5]:
    print("Synset:", synset.name())
    print("Meaning:", synset.definition())
    print()
