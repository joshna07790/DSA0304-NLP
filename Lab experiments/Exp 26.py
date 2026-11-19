text = input("Enter English text: ")

translations = {
    "hello": "Bonjour",
    "hello, how are you?": "Bonjour, comment allez-vous ?",
    "good morning": "Bonjour",
    "good night": "Bonne nuit",
    "thank you": "Merci",
    "i love my country.": "J'aime mon pays.",
    "how are you?": "Comment allez-vous ?",
    "goodbye": "Au revoir"
}

result = translations.get(text.lower())

if result:
    print("\nFrench Translation:")
    print(result)
else:
    print("\nTranslation not available for this sentence.")
