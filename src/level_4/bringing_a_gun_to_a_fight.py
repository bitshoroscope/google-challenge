from math import sqrt, atan2, trunc

def get_sequence(me, soldier, wall, power):
    pos = __simmetry_pos(me, soldier, wall, power)
    neg = __simmetry_neg(pos)
    if soldier == 0:
        neg.pop()
    return neg + pos



def __simmetry_pos(me, soldier, wall, power):
    point = soldier
    if point == 0:
        return [i for i in range(soldier, soldier + power + wall, wall)]
    inc_long = (wall - soldier) * 2
    inc_short = soldier * 2
    points = [soldier]
    while point < me + power:
        point += inc_long
        __append_point(point, points, power, me)

        point += inc_short
        __append_point(point, points, power, me)
    return points

def __simmetry_neg(points):
    negs = [i*-1 for i in points]
    negs.sort()
    return negs


def __append_point(point, points, power, start):
    if (point <= start + power):
        points.append(point)

## Math
def calculate_distance(x2,y2,x1,y1):
    return sqrt((x2-x1)**2+(y2-y1)**2)

def calculate_ankle(x1,y1,x2,y2):
    return truncate(atan2(y2 - y1, x2 - x1), 10)

## Utils
def truncate(number, decimals=0):
    factor = 10.0 ** decimals
    return trunc(number * factor) / factor

## Matrices
def generate_matrix(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power):
    x = get_sequence(me_x, soldier_x, wall_x, power)
    y = get_sequence(me_y, soldier_y, wall_y, power)

    radius = calculate_distance(me_x, me_y, me_x + power, me_y)

    for i in x:
        for j in y:
            coord = (i,j)
            if calculate_distance(me_x, me_y, i, j) <= radius and me_x != i and me_y != j:
                yield coord


def hits_firts(me_x, me_y, matrix, soldier_x, soldier_y, ankle_soldier):
    distance_to_soldier = calculate_distance(me_x, me_y, soldier_x, soldier_y)
    for copy in matrix:
        copy_x = copy[0]
        copy_y = copy[1]
        ankle_me = calculate_ankle(me_x, me_y, copy_x, copy_y)
        if ankle_me == ankle_soldier and calculate_distance(me_x, me_y, copy_x, copy_y) < distance_to_soldier:
            return True
    return False

def hits_first_corner(ankle,distance_to_soldier, ankles_to_corners, distances_to_corners):
    if ankle not in ankles_to_corners:
        return False
    if distances_to_corners[0] < distance_to_soldier and distances_to_corners[1] < distance_to_soldier and \
        distances_to_corners[2] < distance_to_soldier and distances_to_corners[3] < distance_to_soldier:
            return True
    return False

def get_distances_to_corners(me_x, me_y, corners):
    distances = []
    for corner in corners:
        distance = calculate_distance(me_x, me_y, corner[0], corner[1])
        distances.append(distance)
    return distances

def get_ankles_to_corners(me_x, me_y, corners):
    ankles_to_corners = []
    for corner in corners:
        ankle = calculate_ankle(me_x, me_y, corner[0], corner[1])
        ankles_to_corners.append(ankle)
    return ankles_to_corners


def get_possibilities(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y,power, dict_ankles):
    count = 0
    ankles = set()
    corners = [[0, 0], [wall_x, 0], [0, wall_y], [wall_x, wall_y]]
    x = get_sequence(me_x, soldier_x, wall_x, power)
    y = get_sequence(me_y, soldier_y, wall_y, power)

    radius = calculate_distance(me_x, me_y, me_x + power, me_y)
    ankles_to_corners = get_ankles_to_corners(me_x, me_y, corners)
    distances_to_corners = get_distances_to_corners(me_x, me_y, corners)

    for soldier_x in x:
        for soldier_y in y:
            distance_candidate = calculate_distance(me_x, me_y, soldier_x, soldier_y)
            if distance_candidate <= radius and me_x != soldier_x and me_y != soldier_y:
                ankle = calculate_ankle(me_x, me_y, soldier_x, soldier_y)
                me_copy = dict_ankles.get(ankle)
                if me_copy is None:
                    distance_me_to_copy = float('inf')
                else:
                    distance_me_to_copy = calculate_distance(me_x, me_y, me_copy[0], me_copy[1])
                if distance_candidate <= power and ankle not in ankles and distance_me_to_copy > distance_candidate:
                    if hits_first_corner(ankle, distance_candidate, ankles_to_corners, distances_to_corners):
                        continue
                    ankles.add(ankle)
                    count +=1
    return count

def get_ankles_between_me_and_copies(me_x, me_y, mes):
    ankles = {}
    for copy in mes:
        copy_x = copy[0]
        copy_y = copy[1]
        me = (copy_x, copy_y)
        ankle = calculate_ankle(me_x, me_y, copy_x, copy_y)
        if ankle not in ankles:
            ankles[ankle] = me
        else:
            me_copy = ankles.get(ankle)
            distance_actual = calculate_distance(me_x, me_y, me_copy[0], me_copy[1])
            distance_candidate = calculate_distance(me_x, me_y, copy_x, copy_y)
            if distance_candidate < distance_actual:
                ankles[ankle] = me

    return ankles


def solution(dimensions, your_position, trainer_position, distance):
    wall_x = dimensions[0]
    wall_y = dimensions[1]
    me_x = your_position[0]
    me_y = your_position[1]
    soldier_x = trainer_position[0]
    soldier_y = trainer_position[1]

    if(wall_x <= 0 or wall_y <= 0 or me_x < 0 or me_y < 0 or soldier_x < 0 or soldier_y < 0):
        return 0

    if(me_x == soldier_x and me_y == soldier_y):
        return 0

    mes = list(generate_matrix(wall_x, wall_y, me_x, me_y, me_x, me_y, distance))
    ankles = get_ankles_between_me_and_copies(me_x, me_y, mes)

    possibilities = get_possibilities(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, distance, ankles)

    if me_x == soldier_x:
        if calculate_distance(soldier_x, soldier_y, me_x, me_y) <= distance:
            possibilities +=1

    if me_y == soldier_y:
        if calculate_distance(soldier_x, soldier_y, me_x, me_y) <= distance:
            possibilities +=1

    return possibilities
