def solution(n):
    #return control_mechanism(int(n), 0)
    return get_steps(n)


def is_better_subtract(num):
    return num == 3 or num & 3 == 1


def control_mechanism(n, counter):
    if n == 1:
        return counter
    if n & 1 == 0:
        n >>= 1
    elif is_better_subtract(n):
        n -= 1
    else:
        n += 1
    counter += 1
    return control_mechanism(n, counter)


def get_steps(n):
    steps = 0
    while n > 1:
        if n & 1 == 0:
            n >>= 1
        elif is_better_subtract(n):
            n -= 1
        else:
            n += 1
        steps += 1
    return steps



