from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter a text: ")

sentences = [s.strip() for s in text.split('.') if s.strip()]

if len(sentences) < 2:
    print("Text is too short to evaluate coherence.")
else:
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(sentences)

    scores = []

    for i in range(len(sentences) - 1):
        score = cosine_similarity(vectors[i], vectors[i + 1])[0][0]
        scores.append(score)

    coherence = sum(scores) / len(scores)

    print("\nCoherence Score:", round(coherence, 2))

    if coherence >= 0.3:
        print("The text is coherent.")
    else:
        print("The text is less coherent.")
