def solution(x):
    inverted_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd',
     'c', 'b', 'a']

    length = len(inverted_alphabet)
    res = ''

    for char in x:
        if char in inverted_alphabet:
            index = inverted_alphabet.index(char)
            char = inverted_alphabet[length - index - 1]
        res = res + char
    return res
