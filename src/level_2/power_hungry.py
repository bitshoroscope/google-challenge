def solution(xs):

    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    xs.sort()

    negatives, positives = classify_numbers(xs)

    len_negatives = len(negatives)
    len_positives = len(positives)

    if len_negatives == 0 and len_positives == 0:
        return "0"

    if len_negatives == 1 and len_positives == 0:
        return "0"

    if len_negatives == 0 and len_positives == 1:
        return str(xs[0])


    return str(product_negatives(negatives) * product_positives(positives))


def classify_numbers(xs):
    negatives = []
    positives = []
    try:
        while True:
            xs.remove(0)
    except ValueError:
        pass
    for num in xs:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    return negatives, positives


def product_negatives(list):
    res = 1
    length = len(list)
    if length < 1:
        return 1
    if length % 2 == 0:
        index = len(list)
    else:
        index = len(list) - 1
    aux = 0
    while aux < index:
        res = res * list[aux]
        aux += 1
    return res

def product_positives(list):
    res = 1
    for num in list:
        res = res * num
    return res