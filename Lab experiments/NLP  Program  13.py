from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the'
N -> 'dog'
V -> 'barks'
""")

parser = RecursiveDescentParser(grammar)
sentence = "the dog barks".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
