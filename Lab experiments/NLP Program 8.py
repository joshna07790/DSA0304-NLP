import random

tag_probabilities = {
    "book": {"NN": 0.7, "VB": 0.3},
    "runs": {"VB": 0.8, "NNS": 0.2},
    "the": {"DT": 1.0},
    "student": {"NN": 1.0}
}

text = "the student book runs"
words = text.split()

for word in words:
    if word in tag_probabilities:
        tags = list(tag_probabilities[word].keys())
        probabilities = list(tag_probabilities[word].values())
        tag = random.choices(tags, weights=probabilities, k=1)[0]
        print(word, ":", tag)
    else:
        print(word, ": Unknown")
