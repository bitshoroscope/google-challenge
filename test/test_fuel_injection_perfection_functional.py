from google import fuel_injection_perfection_functional as s


def test_is_better_subtract():
    assert True == s.is_better_subtract(1)
    assert True == s.is_better_subtract(5)
    assert True == s.is_better_subtract(9)
    assert True == s.is_better_subtract(13)
    assert True == s.is_better_subtract(37)
    assert True == s.is_better_subtract(41)
    assert False == s.is_better_subtract(2)
    assert False == s.is_better_subtract(8)

def test_solution_procedural():
    assert 5 == s.get_steps(15)
    assert 5 == s.get_steps(17)
    assert 2 == s.get_steps(4)

def test_solution_functional():
    assert 5 == s.control_mechanism(15,0)
    assert 5 == s.control_mechanism(17,0)
    assert 2 == s.control_mechanism(4,0)

def test_verify_both_solutions():
    assert s.control_mechanism(15, 0) == s.get_steps(15)
    assert s.control_mechanism(17, 0) == s.get_steps(17)
    assert s.control_mechanism(4, 0) == s.get_steps(4)
    assert s.control_mechanism(200, 0) == s.get_steps(200)
    assert s.control_mechanism(10000000, 0) == s.get_steps(10000000)
    assert s.control_mechanism(10000001, 0) == s.get_steps(10000001)
    assert s.control_mechanism(9999999, 0) == s.get_steps(9999999)