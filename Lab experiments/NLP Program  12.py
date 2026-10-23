import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the'
N -> 'cat'
V -> 'runs'
""")

parser = EarleyChartParser(grammar)
sentence = "the cat runs".split()

for tree in parser.parse(sentence):
    print(tree)
