from google import max_product as s


def test_only_negatives():
    input = [2, -3, 1, 0, -5]
    assert 30 == s.solution(input)

def test_negatives_product():
    input = [-5]
    assert 1 == s.product_negatives(input)

    input = [-5,-3]
    assert 15 == s.product_negatives(input)

    input = [-5,-3, 2]
    assert 15 == s.product_negatives(input)

def test_positives_product():
    input = [5]
    assert 5 == s.product_positives(input)

    input = [2,5]
    assert 10 == s.product_positives(input)

    input = [2,5,40]
    assert 400 == s.product_positives(input)

def test_google_case():
    input = [2, 0, 2, 2, 0]
    assert "8" == s.solution(input)

    input = [-2, -3, 4, -5]
    assert "60" == s.solution(input)

def test_andy():
    all_negs_odd = [-5,-4,-3,-2]
    assert "120" == s.solution(all_negs_odd)

    all_negs_even = [-6,-5,-4,-3,-2]
    assert "360" == s.solution(all_negs_even)

    all_pos = [5,4,3,2]
    assert "120" == s.solution(all_pos)

    a_neg = [-2,5,4,3,2]
    assert "120" == s.solution(a_neg)

    a_pos = [-6,-5,-4,-3,2,0]
    assert "720" == s.solution(a_pos)

    single_pos = [5]
    assert "5" == s.solution(single_pos)

    all_zeros = [0,0,0,0,0]
    assert "0" == s.solution(all_zeros)

def test_single_neg():
    single_neg = [-5]
    assert "0" == s.solution(single_neg)



