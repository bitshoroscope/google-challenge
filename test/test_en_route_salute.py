from google import en_route_salute as s


def test_salute():
    input = '<'
    assert 0 == s.solution(input)

    input = '>----<'
    assert 2 == s.solution(input)

    input = '<<>><'
    assert 4 == s.solution(input)


def test_clean_input():
    input = '>----<'
    assert '><' == s.clean_input(input)

    input = '<<---->>'
    assert '' == s.clean_input(input)

def test_long_string():
    input = '>>><<<><'
    assert 26 == s.solution(input)

    input = '>><><'
    assert 10 == s.solution(input)

    input = '>><><<'
    assert 16 == s.solution(input)

