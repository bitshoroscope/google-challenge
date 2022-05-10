def solution(n):
    if len(n) > 309:
        sanitized = n[309:]
        assert 309 == len(sanitized)
    else:
        sanitized = n
    res = control_mechanism(int(sanitized), [])
    return len(res) - 1

def control_mechanism(n, list):
    if n % 2 != 0:
        list.append(n)
    if n % 2 != 0:
        n -= 1
    list.append(n)
    n //= 2
    if n == 1:
        list.append(n)
        return list
    else:
        return control_mechanism(n, list)

def generate_list(n, list):
    n -= 1
    list.append(1)
    if n == 0:
        return list
    else:
        return generate_list(n, list)


def generate_list_decremental(n, list):
    n -= 1
    list.append(n + 1)
    if n == 0:
        return list
    else:
        return generate_list_decremental(n, list)

def generate_list_incremental(n, list, counter):
    n -= 1
    counter += 1
    list.append(counter)
    if n == 0:
        return list
    else:
        return generate_list_incremental(n, list, counter)

#print(generate_list_incremental(5, [],0))

def generate_list_incremental2(n, list):
    n -= 1
    list.append(len(list) + 1)
    if n == 0:
        return list
    else:
        return generate_list_incremental2(n, list)


# print(generate_list_incremental2(5,[]))

# print(solution('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'))
print(solution('17'))

# 17 - 18 - 9 - 10 - 5 - 6 - 3 - 4 - 2 - 1
# 17 - 16 - 8 - 4 - 2 - 1