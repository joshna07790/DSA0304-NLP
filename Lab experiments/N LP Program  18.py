import re

def parse(expression):
    pattern = r'^(forall|exists)\s+[a-z]\s*\(\s*[A-Za-z]+\([a-z]\)\s*\)$'

    if re.match(pattern, expression):
        print("Valid FOPC expression")
    else:
        print("Invalid FOPC expression")

parse("forall x (Human(x))")
parse("exists y (Student(y))")
parse("Human x")
