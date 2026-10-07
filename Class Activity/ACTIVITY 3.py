def fsa_bca(string):
    state = 'q0'

    for ch in string:
        if state == 'q0':
            if ch == 'b':
                state = 'q1'
            else:
                state = 'q0'

        elif state == 'q1':
            if ch == 'c':
                state = 'q2'
            else:
                state = 'q0'

        elif state == 'q2':
            if ch == 'a':
                state = 'q3'
            else:
                state = 'q0'

        elif state == 'q3':
            state = 'q3'

    return state == 'q3'


# Multiple inputs
inputs = ["bca", "abca", "bcabc", "bbca", "abc", "bcb", "bcaab"]

for string in inputs:
    if fsa_bca(string):
        print(string, "-> True")
    else:
        print(string, "-> False")
