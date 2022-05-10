from decimal import Decimal, localcontext


def solution(s):
    return str(calculate_sum(Decimal(s)))


def calculate_sum(n):
    with localcontext() as ctx:
        ctx.prec = 200
        two_sqrt = Decimal(2).sqrt()
        alpha = Decimal(n)
        if n == 0:
            return 0
        else:
            n_prime = int((two_sqrt - 1) * alpha)
            return Decimal(Decimal(alpha * Decimal(n_prime)) + Decimal((alpha*(alpha+1)//2)) - Decimal((n_prime * (n_prime + 1))//2) - Decimal(calculate_sum(n_prime)))



print(solution('10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))