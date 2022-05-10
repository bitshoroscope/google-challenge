def solution(s):
    lt = 0
    salutes = 0
    cleaned = clean_input(s)
    for char in cleaned:
        if char == '<':
            lt += 1
    for char in cleaned:
        if char == '>':
            salutes += lt
        else:
            lt -= 1

    return salutes * 2


def clean_input(s):
    return s.replace('-','').lstrip('<').rstrip('>')