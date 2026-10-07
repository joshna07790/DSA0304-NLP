def fsa_aa(string):
    state = 'q0'

    for ch in string:
        if state == 'q0':
            if ch == 'a':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q1':
            if ch == 'a':
                state = 'q2'
            else:
                state = 'q0'

        elif state == 'q2':
            if ch == 'a':
                state = 'q2'
            else:
                state = 'q0'

    return state == 'q2'


# Multiple inputs
inputs = ["aa", "baa", "aabaa", "abab", "abc", "aaa", "bba"]

for string in inputs:
    if fsa_aa(string):
        print(string, "-> true")
    else:
        print(string, "-> false")
