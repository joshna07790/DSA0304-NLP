import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptrer_tagger_eng')
nltk.download('punkt_tab')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)
tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = RegexpParser(grammar)

tree = parser.parse(tags)

print("\nNoun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print(" ".join(word for word, tag in subtree.leaves()))
