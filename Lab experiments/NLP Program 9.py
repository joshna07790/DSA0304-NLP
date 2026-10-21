import re

text = "The student is playing happily"
words = text.split()

patterns = [
    (r".*ing$", "VBG"),
    (r".*ly$", "RB"),
    (r".*ed$", "VBD"),
    (r"^(the|a|an)$", "DT"),
    (r"^(is|are|was|were)$", "VB"),
    (r".*", "NN")
]

for word in words:
    tag = "NN"

    for pattern, pos in patterns:
        if re.fullmatch(pattern, word.lower()):
            tag = pos
            break

    print(word, ":", tag)
