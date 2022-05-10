from google import simmetry as sim
import math

def test_simmetry():
    start = 2
    wall = 5
    power = 5
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [2]

    start = 2
    wall = 3
    power = 5
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [2, 4]

    start = 1
    wall = 6
    power = 34
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [1, 11, 13, 23, 25, 35]

    start = 1
    wall = 3
    power = 14
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [1, 5, 7, 11, 13]

    start = 2
    wall = 4
    power = 15
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [2, 6, 10, 14]

    start = 0
    wall = 3
    power = 15
    me = 1
    assert sim.simmetry_pos(me, start, wall, power) == [0, 3, 6, 9, 12, 15]

def test_neagative_simmetry():
    start = 2
    wall = 4
    power = 15
    points = sim.simmetry_pos(start, wall, power)
    neg_points = sim.simmetry_neg(points)
    assert neg_points == [-2,-6,-10,-14]

    start = 2
    wall = 3
    power = 10
    points = sim.simmetry_pos(start, wall, power)
    neg_points = sim.simmetry_neg(points)
    assert neg_points == [-2, -4, -8, -10]

    start = 0
    wall = 3
    power = 15
    points = sim.simmetry_pos(start, wall, power)
    neg_points = sim.simmetry_neg(points)
    assert neg_points == [0,-3,-6,-9,-12,-15]

def test_get_sequence():
    assert sim.get_sequence(2, 3, 9) == [-10, -8, -4, -2, 2, 4, 8, 10]
    assert sim.get_sequence(0, 3, 9) == [-9, -6, -3, 0, 3, 6, 9]


def test_matrix_points():
    res = sim.get_soldier_matrix(3, 2, 1, 1, 2, 1, 7)
    print(sorted(res,reverse=True))
    # assert [(8, 7), (8, 5), (8, 3), (8, 1), (8, -1), (8, -3), (8, -5), (8, -7), (4, 7), (4, 5), (4, 3), (4, 1), (4, -1), (4, -3), (4, -5), (4, -7), (2, 7), (2, 5), (2, 3), (2, 1), (2, -1), (2, -3), (2, -5), (2, -7), (-2, 7), (-2, 5), (-2, 3), (-2, 1), (-2, -1), (-2, -3), (-2, -5), (-2, -7), (-4, 7), (-4, 5), (-4, 3), (-4, 1), (-4, -1), (-4, -3), (-4, -5), (-4, -7), (-8, 7), (-8, 5), (-8, 3), (-8, 1), (-8, -1), (-8, -3), (-8, -5), (-8, -7)] == res

def test_each_distance():
    power = 4
    soldiers = sim.get_soldier_matrix(3, 2, 1, 1, 2, 1, 4)
    soldiers_sorted = sorted(soldiers)
    print(sim.get_possibilities(1, 1, soldiers_sorted, power))

def test_solution():
    assert 0 == sim.solution([10,10], [2,1], [1, 9], 8)
    assert 0 == sim.solution([10,10], [2,1], [2, 1], 8)
    assert 0 == sim.solution([3,2], [2,1], [20, 1], 10)
    assert 1 == sim.solution([10,10], [2,1], [10, 1], 8)
    assert 1 == sim.solution([10,10], [2,1], [2, 9], 8)
    assert 2 == sim.solution([10,10], [2,1], [10, 1], 10)
    assert 7 == sim.solution([3,2], [1,1], [2,1], 4)
    assert 7 == sim.solution([3,3], [1,1], [2,2], 5)
    assert 8 == sim.solution([23,10], [6,4], [3,2], 23)
    assert 9 == sim.solution([2,2], [1,1], [2,1], 5)
    assert 9 == sim.solution([300,275], [150,150], [185,100], 500)
    assert 10 == sim.solution([3, 2], [2, 2], [1, 1], 5)
    assert 11 == sim.solution([10,2], [2,1], [9, 1], 10)
    assert 12 == sim.solution([2, 2], [2, 2], [1, 1], 5)
    assert 13 == sim.solution([3,3], [2,1], [1, 1], 7)
    assert 13 == sim.solution([5,5], [3,1], [1, 3], 10)
    assert 14 == sim.solution([5,4], [3,1], [1,3], 10)
    assert 15 == sim.solution([4,4], [2,2], [1,3], 10)
    assert 17 == sim.solution([4, 4], [2, 2], [2, 3], 10)
    assert 19 == sim.solution([3,2], [2,1], [1, 1], 7)
    assert 23 == sim.solution([3,2], [2,1], [9, 1], 10)
    assert 25 == sim.solution([3, 3], [1, 1], [2, 2], 10)
    assert 27 == sim.solution([2,5], [1,2], [1,4], 11)
    assert 2553 == sim.solution([3, 3], [1, 1], [2, 2], 100)

def test_out_of_the_box():
    # assert 7399 == sim.solution([10,10], [4,4], [3,3], 500)
    assert 739323 == sim.solution([10,10], [4,4], [3,3], 5000)
    # assert 2957613 == sim.solution([10,10], [4,4], [3,3], 10000)


def test_copies():
    # assert 8 == sim.solution([23,10], [6,4], [3,2], 23)
    # assert 7 == sim.solution([2,5], [1,2], [1,4], 5)
    assert 43 == sim.solution([2,5], [1,2], [1,4], 15)


def test_atan():
    x1 = 1
    y1 = 0
    x2 = 6
    y2 = 5
    myradians = round(math.atan2(y2 - y1, x2 - x1),4)
    print(myradians)

    x1 = 1
    y1 = 0
    x2 = 2
    y2 = 1
    myradians = round(math.atan2(y2 - y1, x2 - x1),4)
    print(myradians)

    x1 = 2
    y1 = 1
    x2 = 1
    y2 = 0
    myradians = round(math.atan2(y2 - y1, x2 - x1),4)
    print(myradians)

def test_wall_sequence():
    wall_x = 2
    wall_y = 5
    me_x = 0
    me_y = 0
    soldier_x = 0
    soldier_y = 0
    wall_x_seq = sim.get_sequence(me_x, soldier_x, wall_x, 10)
    wall_y_seq = sim.get_sequence(me_y, soldier_y, wall_y, 10)

    assert [-10, -8, -6, -4, -2, 0, 2,4,6,8,10] == wall_x_seq
    assert [-10, -5, 0, 5, 10] == wall_y_seq

def test_vertex_array():
    wall_x = 3
    wall_y = 3
    power = 5
    me_x = 1
    me_y = 1
    vertex = sim.get_vertex_matrix(wall_x, wall_y, me_x, me_y, power)
    debug_x = []
    debug_y = []
    # for i in vertex:
    #     debug_x.append(i[0])
    #     debug_y.append(i[1])
    # print(f'x = {debug_x}')
    # print(f'y = {debug_y}')
    print(sorted(vertex))
    assert [(-3, 0), (-3, 3), (0, -3), (0, 0), (0, 3), (3, -3), (3, 0), (3, 3)] == sorted(vertex)



def test_pass_throgh_vertex():
    wall_x = 2
    wall_y = 5
    power = 10
    vertex = sim.get_vertex_matrix(wall_x, wall_y, power)

def test_get_sequence_mes():
    me_x = 2
    me_y = 1
    soldier_x =5
    soldier_y = 7
    wall_x = 3
    wall_y = 2
    power = 7
    assert {(4, 5), (4, 3)} == sim.get_mes_between_origin_and_soldier(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)

    soldier_x =5
    soldier_y = -3
    assert {(4, -1)} == sim.get_mes_between_origin_and_soldier(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)

    soldier_x = -5
    soldier_y = 7
    assert {(-4, 5), (-2, 3), (-4, 3), (-2, 5)} == sim.get_mes_between_origin_and_soldier(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)

    soldier_x = -5
    soldier_y = -5
    assert {(-4, -3), (-4, -1), (-2, -3), (-2, -1)} == sim.get_mes_between_origin_and_soldier(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)

def test_walls():
    wall_x = 3
    wall_y = 3
    me_x = 1
    me_y = 1
    soldier_x = -4
    soldier_y = 7
    power = 8
    print(sim.get_corners_between_origin_and_soldier(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power))

