import spacy

nlp = spacy.load("en_core_web_sm")

text = "Sundar Pichai works at Google in California."
doc = nlp(text)

for entity in doc.ents:
    print(entity.text, "-", entity.label_)
