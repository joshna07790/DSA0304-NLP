import nltk
nltk.download("wordnet")
nltk.download("punkt")

from nltk.wsd import lesk

sentence = "I deposited money in the bank"
word = "bank"

sense = lesk(sentence.split(), word)

if sense:
    print("Word:", word)
    print("Meaning:", sense.definition())
else:
    print("No meaning found")
