size = 0
answer = []


def solution(times, times_limit):
    global answer
    global size
    n = len(times)

    if (n <= 2 or n != len(times[0])):
        return []

    save_all_bunnies = exists_negative_cycles(times, n)
    if(save_all_bunnies):
        for i in range (0,n-2):
            answer.append(i)
        return answer

    else:
        size = 0
        answer = []
        visited = [False] * n
        visited[0] = True
        for i in range(1, n-1):
            candidates = []
            search_path(i, times_limit - times[0][i], times, candidates, visited)
        if len(answer) == 0:
            return []
        else:
            return sorted(answer)

def search_path(vertice, time, times, my_list, visited):
    global size
    global answer
    n = len(times)
    if (time <= -999 or (vertice == n - 1 and time < 0) or size == n - 2):
        return
    if (time >= 0 and vertice == n -1):
        if len(my_list) > size:
            answer = list(my_list)
            size = len(my_list)
        return
    if(visited[vertice]):
        return
    visited[vertice] = True
    my_list.append(vertice - 1)
    for actual in range(1, n):
        if actual == vertice:
            continue
        search_path(actual, time - times[vertice][actual], times, my_list, visited)
    del my_list[len(my_list) - 1]
    visited[vertice] = False

def exists_negative_cycles(times, rows):
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]
    for i in range(0, rows):
        if times[i][i] < 0:
            return True
    return False