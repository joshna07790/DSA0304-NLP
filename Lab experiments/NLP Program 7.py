import nltk

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')

text = "The dog runs quickly in the park."

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("Part-of-Speech Tags:")
print(tags)
