text = input("Enter a text: ")

words = text.split()
previous_noun = ""

print("\nReference Resolution:")

for word in words:
    if word.lower() in ["he", "she", "it", "they"]:
        print(word, "refers to", previous_noun)
    elif word.lower() not in ["is", "was", "the", "a", "and"]:
        previous_noun = word
