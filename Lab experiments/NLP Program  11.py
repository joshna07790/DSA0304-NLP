# Simple Top-Down Parser for CFG

grammar = {
    'S': [['a', 'S', 'b'], ['a', 'b']]
}

def parse(symbols, input_string):
    if not symbols:
        return input_string == ""

    first = symbols[0]
    remaining = symbols[1:]

    if first in grammar:
        for production in grammar[first]:
            if parse(production + remaining, input_string):
                return True
        return False

    if input_string.startswith(first):
        return parse(remaining, input_string[len(first):])

    return False


string = input("Enter a string: ")

if parse(['S'], string):
    print("String accepted by the grammar")
else:
    print("String rejected by the grammar")
