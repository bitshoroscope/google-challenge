def solution(x,y):
    steps = 0
    x = int(x)
    y = int(y)
    while x != 1 and y != 1:
        if x == 0 or y == 0:
            return "impossible"
        steps += get_steps(x,y)
        x, y = get_new_factors(x, y)
    if (x == 1 and y > 1) or (y == 1 and x > 1):
        steps += get_last_steps(x,y)
    return str(steps)


def get_steps(x,y):
    return x // y if x > y else y // x


def get_new_factors(x,y):
    return (x % y, y) if x > y else (x, y % x)


def get_last_steps(x,y):
    return x - y if x > y else y - x