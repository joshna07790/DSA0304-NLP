prompt = input("Enter a prompt: ")

if "artificial intelligence" in prompt.lower() or "ai" in prompt.lower():
    text = """Artificial Intelligence is a modern technology.
It enables machines to learn from data.
AI is used in healthcare and education.
It helps automate many tasks.
AI is transforming the future."""

elif "python" in prompt.lower():
    text = """Python is a popular programming language.
It is easy to learn and use.
Python is used in AI and machine learning.
It supports many useful libraries.
Python is helpful for software development."""

else:
    text = "Text generation is the process of producing meaningful text based on a given prompt."

print("\nGenerated Text:")
print(text)
