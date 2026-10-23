from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Python is used in machine learning",
    "Java is another programming language"
]

query = ["Python programming"]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + query)

scores = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()

ranking = scores.argsort()[::-1]

for i in ranking:
    print("Document:", documents[i])
    print("Score:", round(scores[i], 3))
