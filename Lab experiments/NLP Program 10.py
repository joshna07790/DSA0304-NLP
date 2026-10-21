text = "The dogs are running"
words = text.split()

tags = ["NN"] * len(words)

for i, word in enumerate(words):
    if word.lower() in ["the", "a", "an"]:
        tags[i] = "DT"

for i, word in enumerate(words):
    if word.lower() in ["is", "are", "was", "were"]:
        tags[i] = "VB"

for i, word in enumerate(words):
    if word.lower().endswith("ing"):
        tags[i] = "VBG"

# Transformation rule: words ending in 's' after a determiner are nouns
for i, word in enumerate(words):
    if word.lower().endswith("s") and i > 0 and tags[i - 1] == "DT":
        tags[i] = "NNS"

print("Transformation-Based POS Tagging:")
for word, tag in zip(words, tags):
    print(word, ":", tag)
